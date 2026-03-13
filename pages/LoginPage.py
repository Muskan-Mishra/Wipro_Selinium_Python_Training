from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    signin_btn = (By.ID, "signin")

    username_dropdown = (By.ID, "username")
    password_dropdown = (By.ID, "password")

    username_option = "//div[text()='{}']"
    password_option = "//div[text()='{}']"

    login_btn = (By.ID, "login-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, username, password):

        try:
            self.wait.until(
                EC.element_to_be_clickable(self.signin_btn)
            ).click()

            self.wait.until(
                EC.element_to_be_clickable(self.username_dropdown)
            ).click()

            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.username_option.format(username)))
            ).click()

            self.wait.until(
                EC.element_to_be_clickable(self.password_dropdown)
            ).click()

            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.password_option.format(password)))
            ).click()

            self.wait.until(
                EC.element_to_be_clickable(self.login_btn)
            ).click()

            print("Login successful")

        except Exception as e:
            print("Login failed:", e)