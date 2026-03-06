import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestUploadWaits:

    def test_upload_waits(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()

        # ------------------------
        # 1. Implicit Wait (Global)
        # ------------------------
        driver.implicitly_wait(5)  # Applies to all element searches
        print("Implicit wait set to 5 seconds")

        # ------------------------
        # 2. Static Wait / Hard Wait
        # ------------------------
        time.sleep(2)
        print("Static wait for 2 seconds done")

        # ------------------------
        # 3. Explicit Wait
        # ------------------------
        wait = WebDriverWait(driver, 10)  # max wait 10 sec
        upload_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        print("Explicit wait: file input located")

        # ------------------------
        # 4. Fluent Wait / Custom Wait
        # ------------------------
        errors = [NoSuchElementException, ElementNotInteractableException]
        fluent_wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5, ignored_exceptions=errors)

        # Wait until element is displayed and enabled
        fluent_wait.until(lambda d: upload_input.is_displayed() and upload_input.is_enabled())
        print("Fluent wait: file input is visible and enabled")

        # ------------------------
        # Interact with the element
        # ------------------------
        file_path = "C:/path/to/file.txt"  # Replace with your local file path
        upload_input.send_keys(file_path)
        print("File path entered successfully")

        # Click the upload button
        upload_btn = driver.find_element(By.ID, "file-submit")
        upload_btn.click()
        print("Upload button clicked")

        time.sleep(2)  # Wait to see result
        driver.quit()