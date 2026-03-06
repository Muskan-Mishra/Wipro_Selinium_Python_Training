import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_SelectOptions:

    def test_select_one_and_multiple(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        driver.get("https://trytestingthis.netlify.app/")

        # ---------------- SELECT ONE ----------------
        radios = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']"))
        )

        # Click first radio
        radios[0].click()

        # Assert first radio is selected
        assert radios[0].is_selected()

        # Assert only one is selected
        selected_radios = sum(r.is_selected() for r in radios)
        assert selected_radios == 1

        # ---------------- SELECT MULTIPLE ----------------
        checkboxes = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']"))
        )

        # Select all checkboxes
        for chk in checkboxes:
            if not chk.is_selected():
                chk.click()
            assert chk.is_selected()

        # ---------------- DESELECT MULTIPLE ----------------
        for chk in checkboxes:
            if chk.is_selected():
                chk.click()
            assert not chk.is_selected()
        time.sleep(3)

        driver.quit()