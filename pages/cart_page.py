from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    CHECKOUT_BTN = (By.ID, "checkout")
    TITLE = (By.CLASS_NAME, "title")

    def verify_products(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.TITLE, "Your Cart")
        )

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        ).click()