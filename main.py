from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from web_funcs import get_stock_charts, get_pages

# Chrome driver settings
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.page_load_strategy = "eager"

driver = Chrome(options=chrome_options)
driver.set_page_load_timeout(5)


all_charts = {}


source_codes = get_pages(driver, url=f"https://finviz.com/screener.ashx?v=211&f=sh_avgvol_o500,sh_relvol_o0.5,ta_pattern_channelup2&ft=4")
charts = get_stock_charts(source_code=source_codes)
print(charts)
        

