from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self._check_box = '//button[@class="e4uhfkv0 css-10je9jt e4mggex0"]'
        self._product_name_in_overwiew = '//*[@id="__next"]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/span[1]'
        self._product_price_in_overwiew = '//*[@id="__next"]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/span/span/span[1]'
        self._clear_button = '//button[@class="e4uhfkv0 css-tugfqc e4mggex0"]'

    def get_check_box(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._check_box)))
   
    def get_product_name_in_overwiew(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._product_name_in_overwiew)))

    def get_product_price_in_overwiew(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,  self._product_price_in_overwiew)))

    def get_clear_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._clear_button)))
    
    def text_product_name_in_overwiew(self):
        return self.get_product_name_in_overwiew().text
    
    def text_product_price_in_overwiew(self):
        return self.get_product_price_in_overwiew().text
    
    def click_check_box(self):
        self.get_check_box().click()
        print('clear massage')

    def click_clear_button(self):
        self.get_clear_button().click()
        print('clear cart')

    def payment(self):
        self.get_current_page()
        if self.get_check_box():
            self.click_check_box()
            print('cleare msg!')
        name_in_over = self.text_product_name_in_overwiew()
        pr_in_over = self.text_product_price_in_overwiew()
        self.driver.execute_script("window.history.go(-1)")
        self.click_clear_button()
        return name_in_over, pr_in_over
