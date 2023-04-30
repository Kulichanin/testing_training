from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get('https://www.saucedemo.com/')
username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
username.send_keys('standard_user')
print('input user name')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauce')
print('input pass')
author = driver.find_element(By.XPATH, '//input[@id="login-button"]')
author.click()

url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url == get_url
print('Good url')
driver.close()
