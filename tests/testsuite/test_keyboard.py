import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # ✅ IMPORTANT
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Keyboard:

    def test_keyboard(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://www.facebook.com/")
        time.sleep(3)

        actions = ActionChains(driver)

        email = driver.find_element(By.XPATH, "//input[@name='email']")

        # Move → Hold SHIFT → Type HELLO → Release SHIFT
        actions.move_to_element(email) \
               .click() \
               .key_down(Keys.SHIFT) \
               .send_keys("hello") \
               .key_up(Keys.SHIFT) \
               .perform()

        time.sleep(3)
        driver.quit()

