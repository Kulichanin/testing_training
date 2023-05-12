"""
task 5.5 
Range autoritazion
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from login_page import Login_page 

def main():
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.saucedemo.com/')
    sleep(3)

    # Authorication in site
    # Реализовать подключение нескольких пользователей.
    login = Login_page(driver)
    login.authorization('performance_glitch_user', 'secret_saucee')
    # Logout
    sleep(3)
    (WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
                                           '//button[@id="react-burger-menu-btn"]')))).click()

    (WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
                                           '//a[@id="logout_sidebar_link"]')))).click()
    sleep(3)

if __name__ == "__main__":
    main()
