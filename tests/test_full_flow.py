import pytest
import time
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.CheckoutPage import CheckoutPage
from pages.CheckoutShippingPage import CheckoutShippingPage
from pages.ConfirmationPage import ConfirmationPage
from pages.logout_page import LogoutPage
from utilities.Logger import get_logger
from utilities.ExcelUtils import get_login_data

logger = get_logger()

file_path = r"C:/Users/MUSKAN MISHRA/PycharmProjects/Selenium_Python-CapstonProject/test_data/login_data.xlsx"
login_data = get_login_data(file_path)

@pytest.mark.parametrize("username,password", login_data)
def test_full_flow(driver, download_dir, username, password):

    logger.info("Starting Test")

# Page Objects
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)
    shipping_page = CheckoutShippingPage(driver)
    confirmation_page = ConfirmationPage(driver, download_dir=download_dir)
    logout_page = LogoutPage(driver)

    # Login
    logger.info("Login")
    login_page.login(username, password)
    time.sleep(2)

    # Add Product
    logger.info("Add Product")
    product_page.add_product()
    product_page.checkout()
    time.sleep(2)

    # Continue Checkout
    logger.info("Continue Checkout")
    checkout_page.continue_checkout()
    time.sleep(2)

    # Fill Shipping Info
    logger.info("Fill Shipping Address & Submit")
    shipping_page.fill_shipping_auto()
    shipping_page.submit_shipping()
    time.sleep(2)

    # Order Confirmation
    logger.info("Wait for order confirmation page")
    msg, order_id = confirmation_page.get_confirmation_details()
    print(f"Order Confirmation: {msg}, Order ID: {order_id}")
    assert "successfully placed" in msg.lower()
    time.sleep(2)

    # Download Receipt
    logger.info("Download Receipt")
    confirmation_page.download_receipt()
    time.sleep(2)

    # Continue Shopping
    logger.info("Continue Shopping")
    confirmation_page.click_continue_shopping()
    time.sleep(3)

    # Logout
    logger.info("Logout")
    logout_page.logout()
    print("Logout successful")


