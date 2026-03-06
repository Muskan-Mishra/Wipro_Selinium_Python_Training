import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



DOWNLOAD_DIR = r"C:\Users\MUSKAN MISHRA\Downloads"


class Test_Download:

    def test_download(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # ✅ Correct URL (Download page)
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(3)

        # Click alert.jpeg link
        alert = driver.find_element(By.LINK_TEXT, "alert.jpeg")
        alert.click()

        time.sleep(3)

        # Check file exists
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)

        driver.quit()