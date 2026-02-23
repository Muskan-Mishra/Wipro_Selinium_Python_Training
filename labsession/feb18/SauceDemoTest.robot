
*** Settings ***
Library    SeleniumLibrary
Test Setup     Open Application
Test Teardown  Close Browser

*** Variables ***
${URL}         https://www.saucedemo.com/
${BROWSER}     chrome
${USERNAME}    standard_user
${PASSWORD}    secret_sauce
${TIMEOUT}     30s

*** Test Cases ***
Verify Login And Add Product To Cart
    Wait Until Element Is Visible    id=user-name    ${TIMEOUT}
    Input Text    id=user-name    ${USERNAME}
    Input Text    id=password     ${PASSWORD}
    Click Button  id=login-button

    Wait Until Element Is Visible    xpath://span[text()='Products']    ${TIMEOUT}
    Element Should Be Visible        xpath://span[text()='Products']

    Click Button    id=add-to-cart-sauce-labs-backpack

    Wait Until Element Is Visible    class=shopping_cart_badge    ${TIMEOUT}
    Element Text Should Be           class=shopping_cart_badge    1


*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window