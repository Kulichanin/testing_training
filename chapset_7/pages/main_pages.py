from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver, num_product) -> None:
        super().__init__(driver)
        self.driver = driver
        self.num_product = num_product
        self.product = '//*[@id="inventory_container"]/div/div[{self.num_product}]/div[2]/div/a'
        self.cart = '//div[@id="shopping_cart_container"]'


    def get_product(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_cart(self):
        return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH,  self.cart)))


    def click_select_product(self):
        self.get_product.click()
        print('Click product')

    def click_cart(self):
        self.get_cart.click()
        print('Click cart')



    def authorization(self) -> None:
        self.driver.get(self.url)
        self.get_current_page()
        self.input_username('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()

        # Проверка доступа к странице с продуктами. Ожидание элемента Product 10 секунд.
        # В случае неуспешной авторизации в работу вступает обработчик ошибок.
        try:
            """
            check_string = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,  '//span[@class="title"]')))
            assert check_string.text == 'Products'
            print(f'User authorization succesfull!')
            return check_string.text
            """
            check_string = self.assert_word(self.get_main_word(), 'Products')
            return check_string
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
