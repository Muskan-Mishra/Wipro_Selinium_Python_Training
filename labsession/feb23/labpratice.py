import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_GreenKart:

    URL = "https://rahulshettyacademy.com/seleniumPractise/#/"

    def test_add_product_and_checkout(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        try:
            # ---------- OPEN WEBSITE ----------
            driver.get(self.URL)
            time.sleep(2)

            # ---------- SEARCH PRODUCT ----------
            search = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-keyword"))
            )
            search.send_keys("Tomato")
            time.sleep(2)

            # ---------- ADD TO CART ----------
            add_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='ADD TO CART']"))
            )
            add_button.click()
            time.sleep(2)

            # ---------- OPEN CART ----------
            driver.find_element(By.CLASS_NAME, "cart-icon").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
            time.sleep(2)

            # ---------- VERIFY PRODUCT IN CHECKOUT ----------
            product_name = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "product-name"))
            )

            assert "Tomato" in product_name.text

            # ---------- PLACE ORDER ----------
            driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
            time.sleep(2)

        except Exception as e:
            pytest.fail(f"Test Failed: {e}")

        finally:
            driver.quit()