from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager

import time

def locators1():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("name", "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    title = "Swag Labs"
    print(title)
    assert title == driver.title
    time.sleep(3)
    driver.quit()

def locators2():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("name", "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Backpack").click()
    time.sleep(3)
    driver.quit()


def xpath_locators():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://saucedemo.com")
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)
    driver.quit()


def locators4():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://saucedemo.com")
    time.sleep(2)
    driver.find_elements(By.TAG_NAME, 'input')
    driver.find_elements(By.CLASS_NAME, 'form_input')
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    driver.quit()


if __name__ == "__main__":
    # locators1()
    # locators2()
    # xpath_locators()
    locators4()
