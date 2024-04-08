from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://www.bestbuy.com/"
new_url = "https://www.bestbuy.com/site/electronics/outlet-refurbished-clearance/pcmcat142300050026.c?id=pcmcat142300050026"
browser	= webdriver.Chrome()
browser.maximize_window()
browser.get(url)
outlet_el = browser.find_element(By.CSS_SELECTOR, ".universal-nav-link[data-track='BBYOutlets']")
outlet_el.click()
print("User successfully opened a BestBuy Outlet page in the same tab")
time.sleep(5)
browser.quit()

# if browser.find_element(By.CSS_SELECTOR, ".universal-nav-link[data-track='BBYOutlets']") == "https://www.bestbuy.com/site/electronics/outlet-refurbished-clearance/pcmcat142300050026.c?id=pcmcat142300050026":
#     print("Test passed.")
# else:
#     print("Test FAILED.")