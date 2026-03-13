from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    logout_btn = (By.XPATH, "//span[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def logout(self):
        try:
            logout_button = self.wait.until(
                EC.element_to_be_clickable(self.logout_btn)
            )
            logout_button.click()

            print("Logout successful")

        except Exception as e:
            raise Exception(f"Logout failed: {str(e)}")