from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(
        executable_path='./driver/chromedriver',
        options=options)

driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
username.send_keys('standard_user')
print('input user name')

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauc')
print('input pass')

author = driver.find_element(By.XPATH, '//input[@id="login-button"]')
author.click()

warring_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_element = warring_element.text
assert value_warring_element == 'Epic sadface: Username and password do not match any user in this service'
print('Corrected test!')

driver.refresh()
