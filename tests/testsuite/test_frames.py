from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_frame:

    def test_frame(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.switch_to.frame(0)

        driver.find_element(By.ID, "datepicker").click()

        time.sleep(2)
        driver.quit()