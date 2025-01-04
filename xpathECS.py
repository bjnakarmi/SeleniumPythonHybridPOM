# Equals & Contains & Starts-with
from sys import thread_info

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as s
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

def xpathECS():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("name", "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    # Equals Text
    driver.find_element(By.XPATH, "//div[text() = 'Sauce Labs Backpack']").click()
    time.sleep(2)
    # Contains text
    driver.find_element(By.XPATH, "//button[contains(text(),  'Add')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),  'Back')]").click()
    time.sleep(2)
    # StartsWith
    driver.find_element(By.XPATH, "//button[starts-with(@class,'btn')]").click()
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    xpathECS()