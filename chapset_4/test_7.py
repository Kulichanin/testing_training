"""
Test radiobutton and checkbox
"""
from time import sleep
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
print('take checkbox')
# checkbox test
driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]').click()
driver.find_element(By.XPATH, '//label[@for="tree-node-desktop"]').click()
driver.find_element(By.XPATH, "//label[@for='tree-node-downloads']").click()
print('go radiobutton')
sleep(1)
driver.find_element(By.XPATH, '//li[@id="item-2"]').click()
sleep(1)
driver.find_element(By.XPATH, '//label[@for="yesRadio"]').click()
# driver.close()
