"""
Test doubleclick and rightclick
"""
from time import sleep
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
# double click
action = ActionChains(driver)
double = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double).perform()

# right click
right = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right).perform()
