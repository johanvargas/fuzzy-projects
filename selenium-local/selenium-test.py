"""

https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# browser = webdriver.Firefox()
# browser.get('https://www.savoyparkr.com')   

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path=' /Users/johanvargas/Documents/python/selenium-local/', chrome_options=option)

# request
browser.get("https://www.savoyparkr.com")

# try/except
timeout=20

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='emerald']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
"""
# https://sites.google.com/chromium.org/driver/getting-started?authuser=0
import time
from selenium import webdriver

# driver = webdriver.Chrome('/Users/johanvargas/Documents/python/selenium-local/')
driver = webdriver.Chrome()

driver.get('https://www.electricchoice.com/electricity-prices-by-state/')
# driver.get("https://www.savoyparkr.com")

time.sleep(5) # let user see something

search_box = driver.find_element_by_name('tr')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5)

driver.quit()


