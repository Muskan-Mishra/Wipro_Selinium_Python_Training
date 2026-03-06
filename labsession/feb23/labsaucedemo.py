import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_SauceDemo_E2E:

    URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    def test_end_to_end_flow(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)   # increased wait time

        try:
            driver.get(self.URL)

            # LOGIN
            wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys(self.USERNAME)
            driver.find_element(By.ID, "password").send_keys(self.PASSWORD)
            driver.find_element(By.ID, "login-button").click()

            wait.until(EC.url_contains("inventory"))

            # ADD FIRST PRODUCT SPECIFICALLY (more stable)
            wait.until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
            ).click()

            # VERIFY CART COUNT
            badge = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            assert badge.text == "1"

            # GO TO CART
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            wait.until(EC.url_contains("cart"))

            # VERIFY ITEM EXISTS IN CART
            wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
            )

            # CHECKOUT STEP 1
            driver.find_element(By.ID, "checkout").click()
            wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

            driver.find_element(By.ID, "first-name").clear()
            driver.find_element(By.ID, "first-name").send_keys("Muskan")

            driver.find_element(By.ID, "last-name").clear()
            driver.find_element(By.ID, "last-name").send_keys("Mishra")

            driver.find_element(By.ID, "postal-code").clear()
            driver.find_element(By.ID, "postal-code").send_keys("560001")

            driver.find_element(By.ID, "continue").click()

            # WAIT FOR STEP 2 PAGE USING FINISH BUTTON
            wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

            # CONFIRMATION PAGE
            confirmation = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            )

            assert "Thank you" in confirmation.text

            # LOGOUT
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
            ).click()

        except Exception as e:
            pytest.fail(f"Test Failed: {e}")

        finally:
            driver.quit()