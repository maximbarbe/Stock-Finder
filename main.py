from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from web_funcs import get_source_code, get_stock_charts

# Chrome driver settings
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.page_load_strategy = "eager"
driver = Chrome(options=chrome_options)
driver.set_page_load_timeout(5)

all_charts = {}
initial_num = 1
while True:
    source_code = get_source_code(driver=driver, url=f"https://finviz.com/screener.ashx?v=211&f=sh_avgvol_o500,sh_relvol_o0.5,ta_pattern_channelup2&ft=4&r={initial_num}")
    charts = get_stock_charts(source_code=source_code)
    if len(charts) == 1 and list(charts.keys())[0] in all_charts.keys():
        break
    else:
        all_charts = all_charts | charts
        driver.quit()
        driver = Chrome(options=chrome_options)
        driver.set_page_load_timeout(5)
        initial_num += 12


# Make sure to quit the driver when done.
driver.quit()