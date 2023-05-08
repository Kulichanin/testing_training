"""
4.27 Запросить у пользователя номер товара,
а затем отработать всю бизнес логику магазина.
"""

#!TODO Попробовать сделать через ООП. 
# Каждый товар в магазине это как новый обьект который мы создаем через ввод
"""
print('Идентификатор имени товара 1 Sauce Labs Backpack 
print('Идентификатор имени товара 2 Sauce Labs Bike Light 
print('Идентификатор имени товара 3 Sauce Labs Bolt T-Shirt 
print('Идентификатор имени товара 4 Sauce Labs Fleece Jacket 
print('Идентификатор имени товара 5 Sauce Labs Onesie 
print('Идентификатор имени товара 6 Test.allTheThings() T-Shirt (Red) 
"""

"""
Формурование ссылки htnl элемнета для выделения и взаимодействия
//*[@id="inventory_container"]/div/div[1-6]/div[2]/ + 
    + div[1]/a - имя товара
    + div[2]/div - цена товара
    + div[2]/button - кнопка добавления в корзину

"""
"""
Добавление в корзину
'//*[@class="shopping_cart_container"]/a'
"""
"""
print('Информация о товаре в корзине
'//*[@class="inventory_item_name"]' - имя товара
'//*[@class="inventory_item_price"]' - price
"""
"""
данные и проход в оверьб забрать из 4_17
"""

"""
подтверждение товара
'//*[@class="inventory_item_name"]' - имя товара
'//*[@class="inventory_item_price"]' - price
'//*[@class="summary_subtotal_label"]' - price total
"""
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys    
def screenshot() -> str:
    """
    Create screenshot
    return: name screenshot
    """
    driver = webdriver.Chrome(executable_path='./driver/chromedriver')

    now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    name_screen = 'screenshot_' + now_date + '.png'
    driver.save_screenshot('./screen/' + name_screen)
    return name_screen

def main(number:int) -> None:
    option = Options()
    option.add_experimental_option('detach', True) 
    driver = webdriver.Chrome(executable_path='./driver/chromedriver', 
                              options=option)
    # Authorication in site
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(1)
    driver.find_element(
            By.XPATH, 
            '//input[@data-test="username"]').send_keys('standard_user')
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys('secret_sauce')
    password.send_keys(Keys.ENTER)
    print('Authorization successful')
    print(screenshot())
    
    # Adding the selected product to the cart
    product_name = driver.find_element(By.XPATH,f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div/a').text
    product_price = driver.find_element(By.XPATH,f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div[2]/div').text
    print(f'Вы выбрали товар: {product_name}. Со стоимостью: {product_price}')
    driver.find_element(By.XPATH,f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div[2]/button').click()
    print('Товар успешно добавлен в корзину!')
    #!TODO Все ок но надо поправить рабты функции со скриншотом
    """
    #Go to the shopping cart
    driver.find_element(By.XPATH, '//*[@class="shopping_cart_container"]/a').click()
    driver

    #Info product in your cart
    value_your_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text
    value_your_cart_product_2 = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div').text
    value_price_your_cart_product_1 = driver.find_element(
            By.XPATH, 
            '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text
    value_price_your_cart_product_2 = driver.find_element(
            By.XPATH, 
            '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text
    print(value_your_cart_product_1, value_your_cart_product_2, value_price_your_cart_product_1, value_price_your_cart_product_2)
    """


if __name__ == "__main__":
    print("Приветствую тебя в нашем интернет магазине")
    print("Выбери один из следующих товаров и укажите его номер:")
    print('Идентификатор имени товара 1 - Sauce Labs Backpack') 
    print('Идентификатор имени товара 2 - Sauce Labs Bike Light') 
    print('Идентификатор имени товара 3 - Sauce Labs Bolt T-Shirt') 
    print('Идентификатор имени товара 4 - Sauce Labs Fleece Jacket') 
    print('Идентификатор имени товара 5 - Sauce Labs Onesie') 
    print('Идентификатор имени товара 6 - Test.allTheThings() T-Shirt (Red)')
    number = int(input('Номер товара:'))
    main(number)
