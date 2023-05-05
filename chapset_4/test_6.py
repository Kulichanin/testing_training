"""
Go back page and forward page
"""

from time import sleep
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)


driver.get('https://www.saucedemo.com/')
username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
username.send_keys('standard_user')
print('input user name')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauce')
print('input pass')
author = driver.find_element(By.XPATH, '//input[@id="login-button"]')
author.click()
button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
button.click()
button = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
sleep(1)
button.click()
sleep(1)
driver.back()
print('go back')
sleep(3)
driver.forward()
print('go forward')
sleep(3)
driver.close()
