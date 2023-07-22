from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import time
import requests
import os


def get_source_code(driver: Chrome, url: str) -> BeautifulSoup:
    tags = []
    try:
        driver.get(url=url)
    except:
        print("Error loading the page!")
        quit()
    source_code = driver.execute_script("return document.body.innerHTML")
    html_code: BeautifulSoup = BeautifulSoup(source_code, "html.parser")
    return html_code

def get_stock_charts(source_code: BeautifulSoup) -> dict:
    charts_url = {}
    stocks = source_code.find_all("a", {"class": "border-text"})
    for stock in stocks:
        ticker = get_ticker(stock)
        img_link = get_img_link(stock)
        charts_url[ticker] = img_link
    return charts_url

def get_ticker(stock) -> str:
    return stock.img['alt'].split(" ")[0]
    
def get_img_link(stock) -> str:
    return stock.img['src']

