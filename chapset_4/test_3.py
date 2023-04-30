from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
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
password.send_keys(Keys.RETURN)
print('author sucsess')

filtr = driver.find_element(
        By.XPATH, 
        "//select[@data-test='product_sort_container']"
        )

filtr.click()
filtr.send_keys(Keys.DOWN)
sleep(3)
filtr.send_keys(Keys.RETURN)
sleep(3)

driver.quit()

