from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from pages.cart_page import Cart_page
from pages.client_inf_product import Client_information_pages
from pages.payment_page import Payment_page

def test_select_product():
    # Create driver from webdriver_manager.chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Authorication in site
    login = Login_page(driver)
    login.authorization(username, password)
    print('YES!')
    sleep(3)


def main():
    test_select_product()

if __name__ == '__main__':
    username = input('input username: ')
    password = input('input password: ')
    main()
