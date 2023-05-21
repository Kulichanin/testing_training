from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_pages import Login_page
from pages.main_pages import Main_page

def test_link_about():
    # Create driver from webdriver_manager.chrome 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Authorication in site
    login = Login_page(driver)
    login.authorization()
    
    mp = Main_page(driver)
    mp.select_menu_about()
    sleep(3)


def main():
    test_link_about()

if __name__ == '__main__':
    main()
