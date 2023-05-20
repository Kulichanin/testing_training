from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from pages.cart_page import Cart_page
from pages.client_inf_product import Client_information_pages
from pages.payment_page import Payment_page

def test_select_product(number:int = 3):
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Authorication in site
    login = Login_page(driver)
    login.authorization()
    
    mp = Main_page(driver, number)
    product_name, product_price = mp.select_product()
    
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
    sleep(1)


def main():
    num = input('Введите номер товара: ')
    test_select_product(int(num))

if __name__ == '__main__':
    main()
