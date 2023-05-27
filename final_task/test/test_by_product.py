from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page

def test_select_product(set_up):
    # Input login and username
    username = input('input username: ')
    password = input('input password: ')
    name_product = input('input product: ')
    # Create driver from webdriver_manager.chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Authorication in site
    login = Login_page(driver)
    login.authorization(username, password)
    select_product = Main_page(driver)
    name_pr, price_pr = select_product.select_product(name_product)
    print(name_pr, price_pr)
    sleep(1)
    cart_product = Cart_page(driver)
    name_pr_cart, price_pr_cart = cart_product.product_cart()
    print(name_pr_cart, price_pr_cart)
    sleep(1)
if __name__ == '__main__':
    test_select_product('set_up')

