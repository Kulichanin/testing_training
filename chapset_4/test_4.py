from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

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

#Scrool for javascripts.
#sleep(3)
#driver.execute_script("window.scrollTo(0, 500)")
#sleep(3)

#Scrool for move in python cod.
action = webdriver.ActionChains(driver)
red_t_shirt = driver.find_element(
        By.XPATH, 
        '//*[@id="inventory_container"]/div/div[6]/div[2]'
        )
action.move_to_element(red_t_shirt).perform()

now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
name_screen = 'screenshot_' + now_date + '.png'
driver.save_screenshot('./screen/' + name_screen)

driver.close()
