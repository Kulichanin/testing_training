"""
4.24 Взаимодействие с ползунком
"""

from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)


driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')

action = ActionChains(driver)

price = driver.find_element(By.XPATH, '//*[@id="id1"]')
action.click_and_hold(price).move_by_offset(80,0).release().perform()


# driver.close()
