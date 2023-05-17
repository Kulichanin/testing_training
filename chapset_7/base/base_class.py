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
       
