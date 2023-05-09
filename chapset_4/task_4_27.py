"""
4.27 Запросить у пользователя номер товара,
а затем отработать всю бизнес логику магазина.
"""
from selenium import webdriver
from datetime import datetime
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


def screenshot() -> str:
    """
    Create screenshot
    return: name screenshot
    """
    now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    name_screen = 'screenshot_' + now_date + '.png'
    driver.save_screenshot('./screen/' + name_screen)
    return name_screen

def main(number:int) -> None:
    # Authorication in site
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(1)
    driver.find_element(
            By.XPATH, 
            '//input[@data-test="username"]').send_keys('standard_user')
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys('secret_sauce')
    password.send_keys(Keys.ENTER)
    print('Авторизация успешна.')
   
    # Adding the selected product to the cart
    product_name = driver.find_element(By.XPATH,
                                       f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div/a').text
    product_price = driver.find_element(By.XPATH,
                                        f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div[2]/div').text
    print(f'Вы выбрали товар: {product_name}. Со стоимостью: {product_price}')
    driver.find_element(By.XPATH,
                        f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div[2]/button').click()
    print('Товар успешно добавлен в корзину!')
    sleep(1)
    print(screenshot())

    # Go to the shopping cart
    driver.find_element(By.XPATH, 
                        '//*[@class="shopping_cart_container"]/a').click()

    # Save info product in your cart
    product_name_in_cart = driver.find_element(By.XPATH, '//*[@class="inventory_item_name"]').text
    product_price_in_cart = driver.find_element(By.XPATH, '//*[@class="inventory_item_price"]').text

    print(f'Информация о продукте в корзине: '
          f'Имя товара: {product_name_in_cart}. '
          f'Стоимость: {product_price_in_cart}.')
    sleep(1)
    print(screenshot())

    # Go to the checkout user information
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    
    # Input information about user
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Ivan')
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('Belekov')
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    
    # Go to the checkout:overwiew
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    
    # Getting data about the name and cost of the goods
    product_name_in_overwiew = driver.find_element(By.XPATH, 
                                                   '//*[@class="inventory_item_name"]').text
    product_price_in_overwiew = driver.find_element(By.XPATH, 
                                                    '//*[@class="inventory_item_price"]').text
    product_price_total_text = driver.find_element(By.XPATH, 
                                                    '//*[@class="summary_subtotal_label"]' ).text
    
    product_price_total = product_price_total_text.split('$')

    print(f'Информация о продукте на странице подтверждения товара: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    sleep(1)
    print(screenshot())

    # Checking the name of the cost of goods from all stages
    assert product_name == product_name_in_overwiew == product_name_in_cart
    print('Тест имени товара успешный!')
    assert float(product_price[1:]) == float(product_price_in_cart[1:]) == float(product_price_in_overwiew[1:])  == float(product_price_total[1])
    print('Тест стоимости товара успешный!')

    # Final page
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    print(f'Поздравялем! Вы успешно приобрели товар: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    sleep(1)
    print(screenshot())
    print('Все скриншоты вашего оформления находятся в каталоге: ./screen/')
    driver.close()


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
    
    option = Options()
    option.add_experimental_option('detach', True) 
    driver = webdriver.Chrome(executable_path='./driver/chromedriver', 
                              options=option)

    main(number)
