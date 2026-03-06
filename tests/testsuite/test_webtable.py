import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_WebTable:

    def test_table_data(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/tables")

        time.sleep(2)

        # Validate rows exist
        rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
        assert len(rows) > 0

        time.sleep(2)

        # Validate columns exist
        cols = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
        assert len(cols) > 0

        time.sleep(2)

        # Validate specific cell (Row 3, Column 4)
        cell_data = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]")
        assert "$100.00" in cell_data.text

        time.sleep(2)
        driver.quit()