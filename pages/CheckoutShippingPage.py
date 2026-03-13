from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutShippingPage:

    first_name = (By.XPATH, "//label[text()='First Name']/following-sibling::input")
    last_name = (By.XPATH, "//label[text()='Last Name']/following-sibling::input")
    address = (By.XPATH, "//label[text()='Address']/following-sibling::input")
    state = (By.XPATH, "//label[text()='State/Province']/following-sibling::input")
    postal_code = (By.XPATH, "//label[text()='Postal Code']/following-sibling::input")
    submit_btn = (By.ID, "checkout-shipping-continue")
    confirmation_msg = (By.ID, "confirmation-message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def fill_shipping_auto(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.first_name))

            self.driver.find_element(*self.first_name).send_keys("John")
            self.driver.find_element(*self.last_name).send_keys("Doe")
            self.driver.find_element(*self.address).send_keys("123 Main Street")
            self.driver.find_element(*self.state).send_keys("New York")
            self.driver.find_element(*self.postal_code).send_keys("10001")

            print("Shipping details filled successfully")

        except Exception as e:
            raise Exception(f"Failed to fill shipping details: {str(e)}")

    def submit_shipping(self):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(self.submit_btn)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", element
            )

            element.click()
            print("Shipping form submitted")

        except Exception as e:
            raise Exception(f"Failed to submit shipping form: {str(e)}")

    def verify_confirmation(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.confirmation_msg)
            ).is_displayed()

        except Exception as e:
            raise Exception(f"Confirmation message not found: {str(e)}")