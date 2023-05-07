"""
4.26 Явное и Неявное ожидание
"""

from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(executable_path='./driver/chromedriver', options=option)
# ожидание всего кода
#driver.implicitly_wait(30)

driver.get('https://demoqa.com/dynamic-properties')

# попытка в течение 30 секунд кликать на элемент
visible_buttom = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
#driver.find_element(By.XPATH,'//button[@id="visibleAfter"]')

# driver.close()
