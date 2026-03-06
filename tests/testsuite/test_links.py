import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Links:

    def test_link(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(3)

        links = driver.find_elements(By.TAG_NAME, "a")

        count = len(links)
        print("Total Links:", count)

        # Print all link names
        for link in links:
            print(link.text)

        time.sleep(2)
        driver.quit()