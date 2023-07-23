from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import requests


HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

# Scrape the source code
def get_pages(driver: Chrome,  url: str) -> list[BeautifulSoup]:
    current_page = 1
    html_source_codes = []
    try:
        # Visit the page
        driver.get(url=url)
    except:
        print("Error loading the page!")
        quit()
    while True:
        html_source_codes.append(extract_html(driver=driver))
        next_page = check_for_next_page(driver, current_page)
        
        if next_page:
            current_page += 1
            next_page.click()
        else:
            break
    return html_source_codes

def check_for_next_page(driver: Chrome, current_page: int):
    pages = driver.find_elements(By.CLASS_NAME, "screener-pages")
    for page in pages:
        if page.text == str(current_page + 1):
            return page
    return None



def extract_html(driver: Chrome) -> BeautifulSoup:
    # Execute a javascript script to get the source code
    source_code = driver.execute_script("return document.body.innerHTML")
    # Parse the code.
    html_code: BeautifulSoup = BeautifulSoup(source_code, "html.parser")
    return html_code

# Create a dict for the stock charts and tickers.
def get_stock_charts(source_code: BeautifulSoup) -> dict:
    charts_url = {}
    # Find all anchor tags with 'border-text', that's how we find the stocks.
    for source in source_code:
        stocks = source.find_all("a", {"class": "border-text"})
        for stock in stocks:
            # Extract the ticker and the image link from the anchor tag.
            ticker = get_ticker(stock)
            img_link = get_img_link(stock)
            if ticker not in charts_url:
                charts_url[ticker] = img_link

    return charts_url

# Function to get the ticker from the alternate name of the image
def get_ticker(stock) -> str:
    return stock.img['alt'].split(" ")[0]

# Function to get the source of the image    
def get_img_link(stock) -> str:
    return stock.img['src']

# Function to download the images from the web
def add_images(ticker: str, url: str) -> None:
    # Headers so we can get the images from the urls

    response = requests.get(url=url, headers=HEADERS).content
    with open(f"./stock/{ticker}.jpg", "wb") as img:
        img.write(response)