from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self.button_cart = '//*[@id="checkout"]'
        #driver.find_element(By.XPATH, ).click()
     
    def get_button_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def click_chekout_button(self):
        self.get_button_cart().click()
        print('Click button cart')

    def product_conformation(self):
        self.get_current_page()
        self.click_chekout_button()
