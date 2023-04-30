# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(
        service=ChromiumService(
            ChromeDriverManager(
                chrome_type=ChromeType.CHROMIUM
                ).install()
            )
        )

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.implicitly_wait(2.5)
title = driver.title
print(title)
