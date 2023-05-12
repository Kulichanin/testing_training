"""
task 5.5 
Range autoritazion
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from login_page import Login_page 

def main():
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.saucedemo.com/')
    sleep(3)
    
    list_login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    password = 'secret_sauce' 
    # Authorication in site
    # Реализовать подключение нескольких пользователей.
    login = Login_page(driver)
    login.authorization_list(list_login, password)
    

if __name__ == "__main__":
    main()
