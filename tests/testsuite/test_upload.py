import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Upload:

    def test_upload(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(3)

        # ✅ Build path safely
        file_path = os.path.abspath(r"C:\Users\MUSKAN MISHRA\Pictures\state1.jpg")

        # ✅ Check file exists before uploading
        assert os.path.exists(file_path), f"File not found: {file_path}"

        browse = driver.find_element(By.ID, "file-upload")
        browse.send_keys(file_path)

        time.sleep(2)

        driver.find_element(By.ID, "file-submit").click()
        time.sleep(2)

        fileupload = driver.find_element(By.TAG_NAME, "h3")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.quit()