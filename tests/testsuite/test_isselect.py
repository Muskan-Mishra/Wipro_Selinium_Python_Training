import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_IsSelected_Text:

    def test_radio_and_checkbox(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        driver.get("https://trytestingthis.netlify.app/")

        # ---------------- RADIO BUTTON ----------------
        radios = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[@type='radio']")
            )
        )

        # Click first radio
        radios[0].click()

        # Validate selected
        assert radios[0].is_selected()

        # Validate only one radio selected
        selected_count = sum(radio.is_selected() for radio in radios)
        assert selected_count == 1


        # ---------------- CHECKBOXES ----------------
        checkboxes = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[@type='checkbox']")
            )
        )

        # Select all checkboxes
        for chk in checkboxes:
            if not chk.is_selected():
                chk.click()
            assert chk.is_selected()

        # Deselect all checkboxes
        for chk in checkboxes:
            if chk.is_selected():
                chk.click()
            assert not chk.is_selected()

        time.sleep(3)
        driver.quit()