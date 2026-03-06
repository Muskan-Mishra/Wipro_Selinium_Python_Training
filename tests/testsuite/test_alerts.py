import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Alerts:

    def test_alerts(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(3)

        # ---------------- JS ALERT ----------------
        simplealt = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']"))
        )
        simplealt.click()

        alert = wait.until(EC.alert_is_present())
        assert alert.text == "I am a JS Alert"
        alert.accept()

        # ---------------- JS CONFIRM ----------------
        confalt = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']"))
        )
        confalt.click()

        alert = wait.until(EC.alert_is_present())
        assert alert.text == "I am a JS Confirm"
        alert.dismiss()

        # ---------------- JS PROMPT ----------------
        promptalt = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']"))
        )
        promptalt.click()

        alert = wait.until(EC.alert_is_present())
        assert alert.text == "I am a JS prompt"

        alert.send_keys("test hello")
        alert.accept()
        time.sleep(2)

        driver.quit()