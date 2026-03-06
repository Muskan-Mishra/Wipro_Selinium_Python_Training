import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Scroll:

    def test_scroll(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        driver.get("https://www.amazon.in/")
        time.sleep(4)

        amz = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Amazon Pay on Merchants']")
            )
        )

        # Scroll to element
        driver.execute_script("arguments[0].scrollIntoView();", amz)
        time.sleep(2)

        amz.click()
        time.sleep(3)

        # Scroll up
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        # Scroll down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        driver.quit()