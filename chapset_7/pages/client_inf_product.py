from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Client_information_pages(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self.firts_name = '//*[@id="first-name"]'
        self.last_name = '//*[@id="last-name"]'
        self.zip = '//*[@id="postal-code"]'
        self.continue_button = '//*[@id="continue"]'


    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.firts_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,  self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))
    
    def input_first_name(self, firts_name):
        self.get_first_name().send_keys(firts_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_zip(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print('Input zip code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    def input_information(self):
        self.get_current_page()
        self.input_first_name('Ivan')
        self.input_last_name('Belov')
        self.input_zip('123456')
        self.click_continue_button()
