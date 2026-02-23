
*** Settings ***
Library    SeleniumLibrary
Library    Collections
Suite Setup    Open Browser With Options
Suite Teardown    Close All Browsers

*** Variables ***
${URL}        https://automationexercise.com/
${NAME}       Muskan
${PASSWORD}   Test@123
${EXISTING_EMAIL}   test@test.com
${SEARCH_PRODUCT}   Blue Top

*** Keywords ***

Open Browser With Options
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --disable-notifications
    Call Method    ${chrome_options}    add_argument    --disable-popup-blocking
    Call Method    ${chrome_options}    add_argument    --disable-infobars
    Call Method    ${chrome_options}    add_argument    --start-maximized
    Call Method    ${chrome_options}    add_argument    --disable-extensions
    Open Browser    ${URL}    chrome    options=${chrome_options}
    Set Selenium Timeout    20s
    Wait Until Element Is Visible    xpath=//a[@href="/login"]    20s

Go To Signup Login
    Execute JavaScript    document.querySelector('a[href="/login"]').click()
    Wait Until Element Is Visible    xpath=//input[@data-qa="login-email"]    20s

Register New User
    ${random}=    Evaluate    random.randint(1000,9999)    modules=random
    ${EMAIL}=     Set Variable    muskan${random}@test.com

    Input Text    xpath=//input[@data-qa="signup-name"]    ${NAME}
    Input Text    xpath=//input[@data-qa="signup-email"]   ${EMAIL}
    Click Element    xpath=//button[@data-qa="signup-button"]

    Wait Until Element Is Visible    id=password    20s

    Input Text    id=password    ${PASSWORD}
    Select From List By Value    id=days    10
    Select From List By Value    id=months    5
    Select From List By Value    id=years    1998

    Input Text    id=first_name    Muskan
    Input Text    id=last_name     Mishra
    Input Text    id=address1      Delhi
    Select From List By Label    id=country    India
    Input Text    id=state         Delhi
    Input Text    id=city          Delhi
    Input Text    id=zipcode       110001
    Input Text    id=mobile_number    9999999999

    Click Element    xpath=//button[@data-qa="create-account"]
    Wait Until Element Is Visible    xpath=//b[text()="Account Created!"]    20s
    Click Element    xpath=//a[@data-qa="continue-button"]

Login User
    [Arguments]    ${email}    ${password}
    Input Text    xpath=//input[@data-qa="login-email"]    ${email}
    Input Text    xpath=//input[@data-qa="login-password"]    ${password}
    Click Element    xpath=//button[@data-qa="login-button"]
    Wait Until Element Is Visible    xpath=//a[contains(text(),"Logged in as")]    20s

Logout User
    Execute JavaScript    document.querySelector('a[href="/logout"]').click()
    Wait Until Element Is Visible    xpath=//input[@data-qa="login-email"]    20s

Go To Products
    Execute JavaScript    document.querySelector('a[href="/products"]').click()
    Wait Until Element Is Visible    xpath=//h2[contains(text(),"All Products")]    20s

Go To Contact Us
    Execute JavaScript    document.querySelector('a[href="/contact_us"]').click()
    Wait Until Element Is Visible    xpath=//h2[contains(text(),"Get In Touch")]    20s


*** Test Cases ***

TC_01 Register New User
    Go To Signup Login
    Register New User

TC_02 Login With Existing User
    Go To Signup Login
    Login User    ${EXISTING_EMAIL}    ${PASSWORD}
    Logout User

TC_03 Search Product
    Go To Products
    Input Text    id=search_product    ${SEARCH_PRODUCT}
    Click Element    id=submit_search
    Wait Until Element Is Visible    xpath=//p[contains(text(),"Blue Top")]    20s

TC_04 Contact Us Page
    Go To Contact Us