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
sleep(1)
now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
name_screen = 'screenshot_' + now_date + '.png'
driver.save_screenshot('./screen/' + name_screen)
sleep(1)
#:driver.close()
