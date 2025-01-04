#Writing XPaths using multiple attributes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager

import time

def xpathMul():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    #Using ID or Name
    driver.find_element(By.XPATH, "//*[@id = 'small-searchterms' or @name = 'q']").send_keys("Electronics")
    time.sleep(2)
    #Using ID and Name
    driver.find_element(By.XPATH, "//*[@id = 'small-searchterms' and @name = 'q']").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id = 'small-searchterms' and @name = 'q']").send_keys("Apparels")
    time.sleep(2)
    driver.quit()


#Accessing Xpaths Using Identical HTML elements

def xpathsIdentical():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("name", "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@name, 'add-to-cart')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//button[contains(@name, 'add-to-cart')])[3]").click()
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    # xpathMul()
    xpathsIdentical()