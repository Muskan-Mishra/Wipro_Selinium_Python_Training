import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Action:

    def test_action(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        driver.get("https://www.amazon.in/")
        time.sleep(3)

        actions = ActionChains(driver)

        # -------------------------
        # Double Click - Best Sellers
        # -------------------------
        bestsellers = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
            )
        )
        actions.double_click(bestsellers).perform()
        time.sleep(3)

        driver.back()
        time.sleep(3)

        # -------------------------
        # Right Click - Mobiles
        # -------------------------
        mobiles = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles']")
            )
        )
        actions.context_click(mobiles).perform()
        time.sleep(3)

        # -------------------------
        # Move to Element - Prime
        # -------------------------
        prime = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prime']")
            )
        )
        actions.move_to_element(prime).perform()
        time.sleep(3)

        # -------------------------
        # Click and Hold - Fresh
        # -------------------------
        fresh = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'Fresh')]")
            )
        )
        actions.click_and_hold(fresh).perform()
        time.sleep(3)

        driver.quit()