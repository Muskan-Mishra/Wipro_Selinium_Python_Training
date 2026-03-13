from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ConfirmationPage:
    def __init__(self, driver, download_dir=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

        self.confirmation_msg = (By.ID, "confirmation-message")
        self.order_number = (By.CSS_SELECTOR, "strong")
        self.download_receipt_btn = (By.ID, "downloadpdf")
        self.continue_shopping_btn = (By.CSS_SELECTOR, "button.button--tertiary")

        self.download_dir = download_dir

    def get_confirmation_details(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.confirmation_msg)
        )
        msg = element.text
        order_id = self.driver.find_element(By.CSS_SELECTOR, "strong").text
        return msg, order_id

    def download_receipt(self):
        self.wait.until(
            EC.element_to_be_clickable(self.download_receipt_btn)
        ).click()
        print("Receipt download initiated")
        time.sleep(2)

    def click_continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_shopping_btn)
        ).click()
        print("Clicked Continue Shopping, back to Product Page")