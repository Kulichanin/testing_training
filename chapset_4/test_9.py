"""
lesson date picker
"""
from time import sleep
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)


new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
# clear margin date
for i in range(10):
    new_date.send_keys(Keys.BACKSPACE)

sleep(3)
new_date.send_keys('05/07/2023')

