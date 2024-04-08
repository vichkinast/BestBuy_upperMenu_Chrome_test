from selenium import webdriver
from selenium.webdriver.chrome.service import Service


url = "https://www.bestbuy.com/"
browser	= webdriver.Chrome()
browser.get(url)
print("User successfully opened a webpage: " + browser.current_url)
#find element popup, click block
browser.quit()