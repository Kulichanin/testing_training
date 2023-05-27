from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from time import sleep

class Main_page(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self._products_catalog = '//a[@data-meta-name="DesktopHeaderFixed__catalog-menu"]'
        self._home_appliances_section = 'Бытовая техника'
        self._coffee_mashines_section = '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/section[2]/div/a[4]'
        self._auto_coffee_mashines_section = 'Кофемашины'
        self._find_and_input_filter = '//input[@placeholder="Поиск по фильтрам"]'
        self._checkbox_filter = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/label/span[2]/span/span'
        self._filter_price = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[1]/div[2]/div[2]/div/button[2]/span' #double click
        self._interpreter_name_product = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/a'
        self._interpreter_price_product = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[1]/div[2]/span/span/span[1]' 
        #self._add_to_cart = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[3]/button'
        self._add_to_cart = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[2]/button'
        self._cart = '//button[@class="e4uhfkv0 css-10je9jt e4mggex0"]'


    def get_product_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._products_catalog)))

    def get_home_appliances_section(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self._home_appliances_section)))

    def get_coffee_mashines_section(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._coffee_mashines_section)))

    def get_auto_coffee_mashines_section(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self._auto_coffee_mashines_section)))

    def get_find_and_input_filter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._find_and_input_filter)))
    
    def get_checkbox_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self._checkbox_filter)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._filter_price)))
    
    def get_interpreter_name_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._interpreter_name_product)))
    
    def get_interpreter_price_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._interpreter_price_product)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._cart)))

    def click_product_catalog(self):
        self.get_product_catalog().click()
        print('click product caralog')

    def click_home_appliances_section(self):
        self.get_home_appliances_section().click()
        print('click home appliances section')

    def click_coffee_mashines_section(self):
        self.get_coffee_mashines_section().click()
        print('Click coffee mashines section')

    def click_auto_coffee_mashines_section(self):
        self.get_auto_coffee_mashines_section().click()
        print('Click auto coffee mashines section')
    
    def find_and_input_filter(self, name_company):
        self.get_find_and_input_filter().send_keys(name_company)
        print(f'Input name company {name_company}')
    
    def click_checkbox_filter(self):
        self.get_checkbox_filter().click()
        print('Input filter name company')
        return self.get_checkbox_filter().text

    def click_filter_price(self):
        self.get_filter_price().click()
        print('Click to filter price')

    def find_interpreter_name_product(self):
        return self.get_interpreter_name_product().text

    def find_interpreter_price_product(self):
        return self.get_interpreter_price_product().text
    
    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print('Click add to cart')
    
    def click_go_to_cart(self):
        self.get_cart().click()
        print('Go to cart!')
    

    def select_product(self, name_product):
        self.get_current_page()
        self.click_product_catalog()
        self.click_home_appliances_section()
        self.click_coffee_mashines_section()
        self.click_auto_coffee_mashines_section()
        self.find_and_input_filter(name_product)
        name_filter = self.click_checkbox_filter()
        assert name_filter.lower() == name_product, 'Название фирмы не совпадает!'
        # Пока делал тест нашел баг! Если применять двойной клик на это поле несколько раз, то оно не реагирует после первого нажатия
        self.click_filter_price()
        sleep(1) 
        self.click_filter_price()
        sleep(1)
        name_pr = self.find_interpreter_name_product()
        price_pr = self.find_interpreter_price_product()
        self.get_screenshot()
        sleep(1)
        self.click_add_to_cart()
        sleep(1)
        self.click_go_to_cart()
        return name_pr, price_pr

