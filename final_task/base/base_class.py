from datetime import datetime

class Base():

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_current_page(self):
        """Get current url"""
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    def assert_word(self, word, result):
         """Check assert word"""
         value_word = word.text
         assert value_word == result
         return value_word

    def assert_url(self, result:str):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')


    def get_screenshot(self) -> str:
        """
        Create screenshot
        return: name screenshot
        """
        now_date = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        name_screen = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('./screen/' + name_screen)
        return name_screen
