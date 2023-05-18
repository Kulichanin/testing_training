from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page

def test_select_product(number:int = 3):
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Authorication in site
    login = Login_page(driver)
    login.authorization()
    
    mp = Main_page(driver, number)
    product_name = mp.select_product()

    # Adding the selected product to the cart
    #product_name = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
    #                                   f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div/a')))).text
    product_price = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                        f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div[2]/div')))).text
    print(f'Вы выбрали товар: {product_name}. Со стоимостью: {product_price}')
    #(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
    #                    f'//*[@id="inventory_container"]/div/div[{number}]/div[2]/div[2]/button')))).click()
    print('Товар успешно добавлен в корзину!')
    sleep(1)
    

    # Go to the shopping cart
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, 
                        '//*[@class="shopping_cart_container"]/a')))).click()

    # Save info product in your cart
    product_name_in_cart = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="inventory_item_name"]')))).text
    product_price_in_cart = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="inventory_item_price"]')))).text

    print(f'Информация о продукте в корзине: '
          f'Имя товара: {product_name_in_cart}. '
          f'Стоимость: {product_price_in_cart}.')
    sleep(1)
    

    # Go to the checkout user information
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))).click()
                                                                
    # Input information about user
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="first-name"]')))).send_keys('Ivan')
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="last-name"]')))).send_keys('Belekov')
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="postal-code"]')))).send_keys('123456')
    
    # Go to the checkout:overwiew
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))).click()
    
    # Getting data about the name and cost of the goods
    product_name_in_overwiew = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, 
                                                   '//*[@class="inventory_item_name"]')))).text
    product_price_in_overwiew = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, 
                                                    '//*[@class="inventory_item_price"]')))).text
    product_price_total_text = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, 
                                                    '//*[@class="summary_subtotal_label"]' )))).text
    
    product_price_total = product_price_total_text.split('$')

    print(f'Информация о продукте на странице подтверждения товара: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    sleep(1)
    

    # Checking the name of the cost of goods from all stages
    assert product_name == product_name_in_overwiew == product_name_in_cart
    print('Тест имени товара успешный!')
    assert float(product_price[1:]) == float(product_price_in_cart[1:]) == float(product_price_in_overwiew[1:])  == float(product_price_total[1])
    print('Тест стоимости товара успешный!')

    # Final page
    (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]')))).click()
    print(f'Поздравялем! Вы успешно приобрели товар: ' 
          f'Имя товара: {product_name_in_overwiew}. ' 
          f'Стоимость: {product_price_in_overwiew}.')
    sleep(1)

def main():
    num = input('Введите номер товара: ')
    test_select_product(int(num))
    print('test start')

if __name__ == '__main__':
    main()
