from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get('https://www.saucedemo.com/')
username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
username.send_keys('standard_user')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('secret_sauce')
author = driver.find_element(By.XPATH, '//*[@id="login-button"]')
author.click()
sleep(5)
driver.close()
