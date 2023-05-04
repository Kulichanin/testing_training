from time import sleep
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)

""" Authorization in site """
driver.get('https://www.saucedemo.com/')
sleep(1)

driver.find_element(
        By.XPATH, 
        '//input[@data-test="username"]').send_keys('standard_user')

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('secret_sauce')
password.send_keys(Keys.ENTER)

print('Authorization successful')

""" INFO product first! """
product_1 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
value_product_1 = product_1.text

price_product_1 = driver.find_element(
        By.XPATH, 
        '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div'
        )
value_price_product_1 = price_product_1.text

print('name product: ' + value_product_1, 'price product: ' + value_price_product_1)

add_cart = driver.find_element(
        By.XPATH, 
        '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
        ).click()


""" INFO product second! """
product_2 = driver.find_element(
        By.XPATH, 
        '//*[@id="item_3_title_link"]/div'
        )
value_product_2 = product_2.text

price_product_2 = driver.find_element(
        By.XPATH, 
        '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div'
        )
value_price_product_2 = price_product_2.text

print('name product: ' + value_product_2, 'price product: ' + value_price_product_2)

# cooment add cart 
driver.find_element(
        By.XPATH, 
        '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
# comment basket
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
sleep(1)

#comment
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
"""input information user """
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Ivan')
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('Belekov')
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="continue"]').click()

"""check info product """
value_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text
value_cart_product_2 = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div').text

assert value_product_1 == value_cart_product_1
print('Info cart product 1 Good!')
assert value_product_2 == value_cart_product_2
print('Info cart product 2 Good!')

"""check price product """
value_price_cart_product_1 = driver.find_element(
        By.XPATH, 
        '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text
value_price_cart_product_2 = driver.find_element(
        By.XPATH, 
        '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text

assert value_price_cart_product_1 == value_price_product_1
print('Price cart product 1 Good!')
assert value_price_cart_product_2 == value_price_product_2
print('Price cart product 2 Good!')

"""Check item total"""
item_total = driver.find_element(
        By.XPATH, 
        '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text
item_total_price = item_total.split('$')
assert float(value_price_cart_product_1[1:]) + float(value_price_cart_product_2[1:]) == float(item_total_price[1])
print('Test sum nice!')

"""final test"""
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
sleep(1)
now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
name_screen = 'screenshot_' + now_date + '.png'
driver.save_screenshot('./screen/' + name_screen)
print('Test end!')
driver.close()
