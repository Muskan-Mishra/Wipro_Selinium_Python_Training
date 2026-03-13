from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    first_product = (By.CSS_SELECTOR, "div.shelf-item")
    add_to_cart_btn = (By.CSS_SELECTOR, "div.shelf-item__buy-btn")
    checkout_btn = (By.CLASS_NAME, "buy-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def add_product(self):
        try:
            # Locate product
            product = self.wait.until(
                EC.presence_of_element_located(self.first_product)
            )

            # Find add to cart button
            add_btn = product.find_element(*self.add_to_cart_btn)

            # Scroll to button
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", add_btn
            )

            # Click button
            self.driver.execute_script(
                "arguments[0].click();", add_btn
            )

            print("Product added to cart successfully")

        except Exception as e:
            raise Exception(f"Failed to add product to cart: {str(e)}")

    def checkout(self):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(self.checkout_btn)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", element
            )

            element.click()

            print("Checkout button clicked")

        except Exception as e:
            raise Exception(f"Checkout failed: {str(e)}")