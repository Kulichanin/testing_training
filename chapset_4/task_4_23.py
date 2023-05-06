"""
Task 4.23
"""
from time import sleep
from selenium import webdriver
from datetime import datetime, timedelta

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)

# go to desired url
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)

# search for the desired element
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')

# clear margin date
for i in range(10):
    new_date.send_keys(Keys.BACKSPACE)

# check date now
date_now = datetime.now().strftime("%m/%d/%Y") 
print("date now: " + date_now)

# generate new date plus 10 days
date_plus_10_days = (datetime.now()+timedelta(10)).strftime("%m/%d/%Y")
print("date plus 10 days: " + date_plus_10_days)

# input new date
sleep(3)
new_date.send_keys(date_plus_10_days)
new_date.send_keys(Keys.RETURN)

sleep(3)
driver.close()
