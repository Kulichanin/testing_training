from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver, num_product=None) -> None:
        super().__init__(driver)
        self.driver = driver
        self.menu = "//button[@id='react-burger-menu-btn']"
        self.link_about = "//a[@id='about_sidebar_link']"
        self.product_name = f'//*[@id="inventory_container"]/div/div[{num_product}]/div[2]/div/a'
        self.product_price = f'//*[@id="inventory_container"]/div/div[{num_product}]/div[2]/div[2]/div'
        self.product = f'//*[@id="inventory_container"]/div/div[{num_product}]/div[2]/div[2]/button'
        self.cart = '//*[@class="shopping_cart_container"]/a'


    def get_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,  self.cart)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_menu(self):
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))


    
    def text_product_name(self):
        return self.get_product_name().text
    
    def price_product(self):
        return self.get_product_price().text

    def click_select_product(self):
        self.get_product().click()
        print('Click product')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')
    
    def click_menu(self):
        self.get_menu().click()
        print('Click menu')

    def click_link_about(self):
        self.get_link_about().click()
        print('Click about')

    def select_menu_about(self):
        self.get_current_page()
        self.click_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')

    def select_product(self):
        self.get_current_page()
        self.click_select_product()
        product_name = self.text_product_name()
        product_price = self.price_product()
        self.click_cart()
        return product_name, product_price
