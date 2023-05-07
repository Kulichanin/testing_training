"""
4.25 Отработка исключений
"""

from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)


driver.get('https://demoqa.com/dynamic-properties')
try:
    driver.find_element(By.XPATH,'//button[@id="visibleAfte"]').click()
except NoSuchElementException:
    print('No found element')
# driver.close()
