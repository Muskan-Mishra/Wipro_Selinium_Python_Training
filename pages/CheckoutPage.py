from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    continue_btn = (By.ID, "checkout-shipping-continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def continue_checkout(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.continue_btn)
            ).click()

            print("Continue button clicked successfully")

        except Exception as e:
            raise Exception(f"Failed to click Continue button: {str(e)}")