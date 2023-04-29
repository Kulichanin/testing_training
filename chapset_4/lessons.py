from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get('https://www.saucedemo.com/')
sleep(5)
driver.close()
