from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    INVENTORY_TITLE = (By.CLASS_NAME, "title")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

        # ✅ Ensure login successful
        self.wait.until(
            EC.text_to_be_present_in_element(self.INVENTORY_TITLE, "Products")
        )