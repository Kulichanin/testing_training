from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        
        self._url = 'https://www.citilink.ru/'
        self._user_name = '//input[@name="login"]'
        self._password = '//input[@name="pass"]'
        self._login_button = '//div[@data-meta-name="UserButtonContainer"]'
        self._login_button_enter = '//button[@class="e4uhfkv0 css-1yh1imp e4mggex0"]'
        self._main_word = '//span[@class="title"]'


    def get_user_name(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self._user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH,  self._password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self._login_button)))
    
    def get_login_button_enter(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self._login_button_enter)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self._main_word)))

    def input_username(self, username):
        self.get_user_name().send_keys(username)
        print('Input username')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def click_login_button_enter(self):
        self.get_login_button_enter().click()
        print('Click login button enter')



    def authorization(self, username, password) -> None:
        self.driver.get(self._url)
        self.get_current_page()
        self.driver.maximize_window()
        self.click_login_button()
        self.input_username(username)
        self.input_password(password)
        self.click_login_button_enter()
