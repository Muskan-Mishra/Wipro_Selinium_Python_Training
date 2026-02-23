
*** settings ***
Library    SeleniumLibrary    # Import Selenium library to use browser keywords
Resource    ../Resources/Resources.robot
Test Setup Lunch Browser
Test Teardown Log Close the Browser


*** Test Cases ***
# First Test Case
Verify login with valid credentials
    Login    # Calling user-defined keyword

# Second Test Case
Verify Add to cart functionality
    Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies that the product with details is added to the cart
