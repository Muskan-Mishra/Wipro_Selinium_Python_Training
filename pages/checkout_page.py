from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TITLE = (By.CLASS_NAME, "title")

    def enter_details(self, first, last, postal):

        # ✅ Ensure correct page
        self.wait.until(
            EC.text_to_be_present_in_element(self.TITLE, "Checkout: Your Information")
        )

        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last)
        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(postal)

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BTN)
        ).click()