from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        
        self.url = 'https://www.saucedemo.com/'
        self.user_name = '//input[@data-test="username"]'
        self.password = '//input[@id="password"]'
        self.login_button = '//input[@id="login-button"]'


    def get_user_name(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,  self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def input_username(self, username):
        self.get_user_name().send_keys(username)
        print('Input username')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')



    def authorization(self) -> None:
        self.driver.get(self.url)
        self.input_username('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()

        # Проверка доступа к странице с продуктами. Ожидание элемента Product 10 секунд.
        # В случае неуспешной авторизации в работу вступает обработчик ошибок.
        try:               
            check_string = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,  '//span[@class="title"]')))
            assert check_string.text == 'Products'
            print(f'User authorization succesfull!')
            return check_string.text
        except TimeoutException:
            # Поиcк ошибки и ее вывод к консоль
            check_string_error = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,  '//h3[@data-test="error"]')))
            print(f'User authorization failed! {check_string_error.text}')
     
    def authorization_list(self, user_login_list:list[str], user_pass:str) -> None:
        for i in user_login_list:
            result = self.authorization()
            if result:
                #Если авторизация нормальная, то выходим с помощью log out
                (WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH,'//button[@id="react-burger-menu-btn"]')))).click()

                (WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH,'//a[@id="logout_sidebar_link"]')))).click()

            else:
                # Если с авторизацией проблемы, то перезагружаем страницу.
                # Таким образом логин и пароль очищаются.
                self.driver.refresh()
