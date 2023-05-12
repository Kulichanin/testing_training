"""
task 5.3
Create class login. Delete input login
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
        # В случае неуспешной авторизации в работу вступает обработчик ошибок.
        try:               
            check_string = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,  '//span[@class="title"]')))
            assert check_string.text == 'Products'
            print(f'User {user_login} authorization succesfull!')
            return check_string.text
        except TimeoutException:
            check_string_error = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,  '//h3[@data-test="error"]')))
            # Check succesfull authorization:
            print(f'User {user_login } authorization failed! {check_string_error.text}')
    
    def authorization_list(self, user_login_list:list[str], user_pass:str) -> None:
        for i in user_login_list:
            result = self.authorization(i, user_pass)
            if result:
                (WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH,'//button[@id="react-burger-menu-btn"]')))).click()

                (WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH,'//a[@id="logout_sidebar_link"]')))).click()

            else:
                login_clear = WebDriverWait(self.driver, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '//input[@data-test="username"]')))
                login_clear.clear()
                sleep(1)
                password_clear = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH,  '//input[@id="password"]')))
                password_clear.clear()
                sleep(1)
                
