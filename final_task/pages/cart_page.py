from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self._name_product = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[2]/div/a/span/span'
        self._price_product = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[4]/div/div[2]/span/span/span[1]' 
        self._button_cart = '//*[@id="__next"]/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[1]/div/div[5]/button '

    
    def get_name_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._name_product)))
    
    def get_price_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._price_product)))
    
    def get_button_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._button_cart)))
    
    
    def find_name_product(self):
        return self.get_name_product().text

    def find_price_product(self):
        return self.get_price_product().text
    
    def click_chekout_button(self):
        self.get_button_cart().click()
        print('Click button cart')

    
    def product_cart(self):
        self.get_current_page()
        name_pr = self.find_name_product()
        price_pr = self.find_price_product()
        self.get_screenshot()
        self.click_chekout_button()
        return name_pr, price_pr
