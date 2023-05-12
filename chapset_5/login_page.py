"""
task 5.3
Create class login
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():

    def __init__(self, driver) -> None:
        self.driver = driver

    def authorization(self, user_login:str, user_pass:str) -> None:
        login = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@data-test="username"]')))
        login.send_keys(user_login)
        password = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH,  '//input[@id="password"]')))
        password.send_keys(user_pass)
        login_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH,  '//input[@id="login-button"]')))
        login_button.click()
        # Проверка доступа к странице с продуктами. Ожидание элемента Product 10 секунд.
        # В случае неуспешной авторизации в работу вступает обработчки ошибок.
        try:               
            check_string = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,  '//span[@class="title"]')))
            assert check_string.text == 'Products'
            print('Авторизация успешна.')
        except TimeoutException:
            check_string_error = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,  '//h3[@data-test="error"]')))
            # Check succesfull authorization:
            if (check_string_error.text).startswith('Epic sadface'):
                print(f'Authorization failed!\n{check_string_error.text}')
        
