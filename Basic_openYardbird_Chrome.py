from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://www.bestbuy.com/"
API_url = "https://yardbird.com/"
browser	= webdriver.Chrome()
browser.maximize_window()
browser.get(url)
form_el = browser.find_element(By.XPATH, "//a[normalize-space()='Yardbird']")
form_el.click()
print("User successfully opened a link in a new tab: " + API_url)
time.sleep(5)
browser.quit()