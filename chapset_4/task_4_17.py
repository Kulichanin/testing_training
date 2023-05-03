from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)

# Authorization in site
driver.get('https://www.saucedemo.com/')
sleep(1)

username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
username.send_keys('standard_user')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauce')
password.send_keys(Keys.ENTER)

print('Authorization successful')

""" INFO product first! """
product_1 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
value_product = product_1.text

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text

print('name product: ' + value_product, 'price product: ' + value_price_product_1)

add_cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()


""" INFO product second! """
product_1 = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
value_product = product_1.text

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text

print('name product: ' + value_product, 'price product: ' + value_price_product_1)

add_cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
# sleep(2)
# driver.close()
