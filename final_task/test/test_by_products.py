import pytest

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from pages.cart_page import Cart_page
from pages.client_inf_product import Client_information_pages
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page

#@pytest.mark.order(3)
def test_select_product_3(set_up, number:int = 3):
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Authorication in site
    login = Login_page(driver)
    login.authorization()
    
    mp = Main_page(driver, number)
    product_name, product_price = mp.select_product()
    print('Start test 3')
    
    print(f'Вы выбрали товар: {product_name}. Со стоимостью: {product_price}')
    print('Товар успешно добавлен в корзину!')
    sleep(1)

    cp = Cart_page(driver)
    cp.product_conformation()
    sleep(1)
    
    cli = Client_information_pages(driver)
    cli.input_information()
    sleep(1)

    # Getting data about the name and cost of the goods
    sleep(1)
    pay_page = Payment_page(driver)
    product_name_in_overwiew, product_price_in_overwiew, product_price_total = pay_page.payment()

    # Checking the name of the cost of goods from all stages
    assert product_name == product_name_in_overwiew
    print('Тест имени товара успешный!')
    assert float(product_price[1:])  == float(product_price_in_overwiew[1:])  == float(product_price_total[1])
    print('Тест стоимости товара успешный!')

    # Final page
    print(f'Поздравялем! Вы успешно приобрели товар: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    fin = Finish_page(driver)
    fin.finish()
    sleep(1)
    print('Finish test 3')

#@pytest.mark.order(1)
def test_select_product_1(set_up, number:int = 1):
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Authorication in site
    login = Login_page(driver)
    login.authorization()
    
    mp = Main_page(driver, number)
    product_name, product_price = mp.select_product()
    print('Start test 1')
    
    print(f'Вы выбрали товар: {product_name}. Со стоимостью: {product_price}')
    print('Товар успешно добавлен в корзину!')
    sleep(1)

    cp = Cart_page(driver)
    cp.product_conformation()
    sleep(1)
    
    cli = Client_information_pages(driver)
    cli.input_information()
    sleep(1)

    # Getting data about the name and cost of the goods
    sleep(1)
    pay_page = Payment_page(driver)
    product_name_in_overwiew, product_price_in_overwiew, product_price_total = pay_page.payment()

    # Checking the name of the cost of goods from all stages
    assert product_name == product_name_in_overwiew
    print('Тест имени товара успешный!')
    assert float(product_price[1:])  == float(product_price_in_overwiew[1:])  == float(product_price_total[1])
    print('Тест стоимости товара успешный!')

    # Final page
    print(f'Поздравялем! Вы успешно приобрели товар: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    fin = Finish_page(driver)
    fin.finish()
    sleep(1)
    print('Finish test 1')

#@pytest.mark.order(2)
def test_select_product_2(number:int = 2):
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Authorication in site
    login = Login_page(driver)
    login.authorization()
    
    mp = Main_page(driver, number)
    product_name, product_price = mp.select_product()
    print('Start test 2')
    
    print(f'Вы выбрали товар: {product_name}. Со стоимостью: {product_price}')
    print('Товар успешно добавлен в корзину!')
    sleep(1)

    cp = Cart_page(driver)
    cp.product_conformation()
    sleep(1)
    
    cli = Client_information_pages(driver)
    cli.input_information()
    sleep(1)

    # Getting data about the name and cost of the goods
    sleep(1)
    pay_page = Payment_page(driver)
    product_name_in_overwiew, product_price_in_overwiew, product_price_total = pay_page.payment()

    # Checking the name of the cost of goods from all stages
    assert product_name == product_name_in_overwiew
    print('Тест имени товара успешный!')
    assert float(product_price[1:])  == float(product_price_in_overwiew[1:])  == float(product_price_total[1])
    print('Тест стоимости товара успешный!')

    # Final page
    print(f'Поздравялем! Вы успешно приобрели товар: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    fin = Finish_page(driver)
    fin.finish()
    sleep(1)
    print('Finish test 2')
