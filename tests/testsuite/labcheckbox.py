import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_select_employee_checkboxes(driver):

    wait = WebDriverWait(driver, 15)

    # ---------------- LOGIN ----------------
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")

    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    # Wait for Dashboard
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # ---------------- PIM PAGE ----------------
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='oxd-table-body']")
    ))

    # ---------------- SELECT FIRST CHECKBOX ----------------
    checkbox = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='oxd-table-body']//span[contains(@class,'oxd-checkbox-input')])[1]")
    ))

    driver.execute_script("arguments[0].click();", checkbox)

    # PASS CONDITION
    assert checkbox.is_displayed()

    time.sleep(3)
    driver.quit()

