from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    TITLE = (By.CLASS_NAME, "title")

    def add_products(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.TITLE, "Products")
        )
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        ).click()

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()