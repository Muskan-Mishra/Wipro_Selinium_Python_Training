import pytest
from pages.login_page import loginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.Overview_page import OverviewPage
from utilities.logger import get_logger
from utilities.excel_utils import get_excel_data


logger = get_logger()

file_path = r"C:\Users\MUSKAN MISHRA\PycharmProjects\SeleniumPyteatPOM\testdata\login_data.xlsx"
test_data = get_excel_data(file_path)


class TestSauceDemo:

    @pytest.mark.parametrize("username,password", test_data)
    def test_complete_order_flow(self, driver, username, password):

        logger.info("Starting SauceDemo Test")

        # 1️⃣ Login
        login = LoginPage(driver)
        login.login(username, password)

        # 2️⃣ Inventory
        inventory = InventoryPage(driver)
        inventory.add_products()
        inventory.go_to_cart()

        # 3️⃣ Cart
        cart = CartPage(driver)
        cart.verify_products()
        cart.click_checkout()

        # 4️⃣ Checkout
        checkout = CheckoutPage(driver)
        checkout.enter_details("Muskan", "Mishra", "560067")

        # 5️⃣ Overview
        overview = OverviewPage(driver)
        overview.finish_order()

        # 6️⃣ Validation
        assert overview.verify_success()
        logger.info("Order completed successfully")
