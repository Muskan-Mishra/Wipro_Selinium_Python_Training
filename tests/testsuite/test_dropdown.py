from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_DropDown:

    def test_dropdown(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        dropdown = wait.until(
            EC.presence_of_element_located((By.ID, "dropdown-class-example"))
        )

        sel = Select(dropdown)

        # Select by visible text
        sel.select_by_visible_text("Option1")

        # Select by value (correct lowercase)
        sel.select_by_value("option2")

        # Select by index
        sel.select_by_index(3)

        driver.quit()