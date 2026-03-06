import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Ecommerce:

    def test_register_login_shopping(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        driver.get("https://demowebshop.tricentis.com/")

        # =========================
        # REGISTER
        # =========================
        driver.find_element(By.LINK_TEXT, "Register").click()

        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Muskan")
        driver.find_element(By.ID, "LastName").send_keys("Mishra")

        # ✅ Unique email every run
        email = f"muskan{int(time.time())}@test.com"
        driver.find_element(By.ID, "Email").send_keys(email)

        driver.find_element(By.ID, "Password").send_keys("Test@123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@123")

        driver.find_element(By.ID, "register-button").click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "result")))
        driver.find_element(By.CLASS_NAME, "register-continue-button").click()

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))
        driver.find_element(By.LINK_TEXT, "Log out").click()

        # =========================
        # LOGIN
        # =========================
        driver.find_element(By.LINK_TEXT, "Log in").click()

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys("Test@123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))

        # =========================
        # ADD PRODUCT
        # =========================
        driver.find_element(By.LINK_TEXT, "Books").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@value='Add to cart'])[1]"))).click()

        driver.find_element(By.LINK_TEXT, "Shopping cart").click()

        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()

        # =========================
        # BILLING ADDRESS
        # =========================
        Select(wait.until(
            EC.element_to_be_clickable((By.ID, "BillingNewAddress_CountryId"))
        )).select_by_visible_text("India")

        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Delhi")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Test Street")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("110001")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9999999999")

        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Shipping.save()']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ShippingMethod.save()']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentMethod.save()']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentInfo.save()']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ConfirmOrder.save()']"))).click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "order-completed")))

        print("✅ Order placed successfully!")

        driver.quit()