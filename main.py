from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from web_funcs import get_source_code, get_stock_charts

# Chrome driver settings
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = Chrome(options=chrome_options)
driver.set_page_load_timeout(5)

source_code = get_source_code(driver=driver, url="https://finviz.com/screener.ashx?v=211&f=sh_avgvol_o500,sh_relvol_o0.5,ta_pattern_channelup2&ft=4")
charts = get_stock_charts(source_code=source_code)



# Make sure to quit the driver when done.
driver.quit()