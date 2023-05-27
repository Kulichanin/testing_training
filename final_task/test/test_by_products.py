from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page

def test_select_product_1(set_up_1):
    # Input login and username
    username = input('input username: ')
    password = input('input password: ')
    name_product = input('input product: ')
    # Create driver from webdriver_manager.chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Authorication in site
    login = Login_page(driver)
    login.authorization(username, password)
    # Select product
    select_product = Main_page(driver)
    name_pr, price_pr = select_product.select_product(name_product)
    print(name_pr, price_pr)
    sleep(1)
    # Cart page info
    cart_product = Cart_page(driver)
    name_pr_cart, price_pr_cart = cart_product.product_cart()
    print(name_pr_cart, price_pr_cart)
    sleep(1)
    # Paymanet page info
    paymaent_page = Payment_page(driver)
    paym_name, paym_price = paymaent_page.payment()
    print(paym_name, paym_price)
    sleep(1)
    assert name_pr == name_pr_cart == paym_name, 'Проблема с именем товара!'
    print('Поле имени совпало')
    assert price_pr == price_pr_cart == paym_price, 'Проблема со стоимостью товара!'
    print('Поле стоимости совпало')

def test_select_product_2(set_up_2):
    # Input login and username
    username = input('input username: ')
    password = input('input password: ')
    name_product = input('input product: ')
    # Create driver from webdriver_manager.chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Authorication in site
    login = Login_page(driver)
    login.authorization(username, password)
    # Select product
    select_product = Main_page(driver)
    name_pr, price_pr = select_product.select_product(name_product)
    print(name_pr, price_pr)
    sleep(1)
    # Cart page info
    cart_product = Cart_page(driver)
    name_pr_cart, price_pr_cart = cart_product.product_cart()
    print(name_pr_cart, price_pr_cart)
    sleep(1)
    # Paymanet page info
    paymaent_page = Payment_page(driver)
    paym_name, paym_price = paymaent_page.payment()
    print(paym_name, paym_price)
    sleep(1)
    assert name_pr == name_pr_cart == paym_name, 'Проблема с именем товара!'
    print('Поле имени совпало')
    assert price_pr == price_pr_cart == paym_price, 'Проблема со стоимостью товара!'
    print('Поле стоимости совпало')

def test_select_product_3(set_up_3):
    # Input login and username
    username = input('input username: ')
    password = input('input password: ')
    name_product = input('input product: ')
    # Create driver from webdriver_manager.chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Authorication in site
    login = Login_page(driver)
    login.authorization(username, password)
    # Select product
    select_product = Main_page(driver)
    name_pr, price_pr = select_product.select_product(name_product)
    print(name_pr, price_pr)
    sleep(1)
    # Cart page info
    cart_product = Cart_page(driver)
    name_pr_cart, price_pr_cart = cart_product.product_cart()
    print(name_pr_cart, price_pr_cart)
    sleep(1)
    # Paymanet page info
    paymaent_page = Payment_page(driver)
    paym_name, paym_price = paymaent_page.payment()
    print(paym_name, paym_price)
    sleep(1)
    assert name_pr == name_pr_cart == paym_name, 'Проблема с именем товара!'
    print('Поле имени совпало')
    assert price_pr == price_pr_cart == paym_price, 'Проблема со стоимостью товара!'
    print('Поле стоимости совпало')


if __name__ == '__main__':
    test_select_product_1('set_up_1')
    test_select_product_2('set_up_2')
    test_select_product_3('set_up_3')

