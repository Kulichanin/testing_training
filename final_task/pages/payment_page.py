from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self.product_name_in_overwiew = '//*[@class="inventory_item_name"]'
        self.product_price_in_overwiew = '//*[@class="inventory_item_price"]'
        self.product_price_total = '//*[@class="summary_subtotal_label"]'
        self.finish_button = '//*[@id="finish"]'


    def get_product_name_in_overwiew(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_in_overwiew)))

    def get_product_price_in_overwiew(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,  self.product_price_in_overwiew)))

    def get_product_price_total(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price_total)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))
    
    def text_product_name(self):
        return self.get_product_name_in_overwiew().text
    
    def text_product_price_in_overwiew(self):
        return self.get_product_price_in_overwiew().text

    def text_product_price_total(self):
        product_price_total = self.get_product_price_total().text
        return product_price_total.split("$")

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Click product')

    def payment(self):
        self.get_current_page()
        text_name = self.text_product_name()
        pr_in_over = self.text_product_price_in_overwiew()
        pr_price_total = self.text_product_price_total()
        self.click_finish_button()
        return text_name, pr_in_over, pr_price_total
