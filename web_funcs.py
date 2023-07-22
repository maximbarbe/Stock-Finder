from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import requests


# Scrape the source code
def get_source_code(options: Options, chart_num: int, url: str) -> BeautifulSoup:
    driver = Chrome(options=options)
    driver.set_page_load_timeout(5)
    try:
        # Visit the page
        driver.get(url=url)
    except:
        print("Error loading the page!")
        quit()
    # Execute a javascript script to get the source code
    source_code = driver.execute_script("return document.body.innerHTML")
    # Parse the code.
    html_code: BeautifulSoup = BeautifulSoup(source_code, "html.parser")
    driver.quit()
    return html_code

# Create a dict for the stock charts and tickers.
def get_stock_charts(source_code: BeautifulSoup) -> dict:
    charts_url = {}
    # Find all anchor tags with 'border-text', that's how we find the stocks.
    stocks = source_code.find_all("a", {"class": "border-text"})
    for stock in stocks:
        # Extract the ticker and the image link from the anchor tag.
        ticker = get_ticker(stock)
        img_link = get_img_link(stock)
        charts_url[ticker] = img_link
    return charts_url

# Function to get the ticker from the alternate name of the image
def get_ticker(stock) -> str:
    return stock.img['alt'].split(" ")[0]

# Function to get the source of the image    
def get_img_link(stock) -> str:
    return stock.img['src']

# Function to download the images from the web
def add_images(stocks: dict) -> None:
    pass