from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased timeout

    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")
    TITLE = (By.CLASS_NAME, "title")

    def finish_order(self):
        # Wait until the URL contains "checkout-step-two" to ensure we're on the overview page
        self.wait.until(EC.url_contains("checkout-step-two"))

        # Wait until the Finish button is present in DOM and visible
        finish_btn = self.wait.until(
            EC.presence_of_element_located(self.FINISH_BTN)
        )

        # Scroll into view and click safely
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish_btn)
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def verify_success(self):
        # Wait for success message to appear
        success = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        )
        return "Thank you for your order!" in success.text