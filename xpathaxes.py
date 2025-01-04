from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager

import time

def axes():
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
    driver.maximize_window()
    text_msg = driver.find_element(By.XPATH, "//a[normalize-space()='Ashoka Buildcon Ltd.']/self::a").text
    print(text_msg)
    text_msg1 = driver.find_element(By.XPATH, "//a[normalize-space()='Ashoka Buildcon Ltd.']/parent::td").text
    print(text_msg1)
    text_msg2 = driver.find_element(By.XPATH, "//a[normalize-space()='Ashoka Buildcon Ltd.']/ancestor::tr").text
    print(text_msg2)
    #for all the children of an ancestor and to get the text value, first use find_elements, store the elements in a variable then use loop to access each one.
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    axes()