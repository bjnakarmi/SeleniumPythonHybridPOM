from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager

import time

def browser():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    browser()