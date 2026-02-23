
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.saucedemo.com/
${BROWSER}     chrome
${USERNAME}    standard_user
${PASSWORD}    secret_sauce

*** Test Cases ***
Complete Purchase And Validate Checkout Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    id:user-name    ${USERNAME}
    Input Text    id:password     ${PASSWORD}
    Click Button  id:login-button

    Wait Until Element Is Visible    class:title    10s

    Click Button    id:add-to-cart-sauce-labs-backpack

    Click Element    class:shopping_cart_link

    Wait Until Element Is Visible    id:checkout    10s
    Click Button    id:checkout

    Input Text    id:first-name    Priyadarshee
    Input Text    id:last-name     Kumar
    Input Text    id:postal-code   826001
    Click Button  id:continue

    Wait Until Element Is Visible    id:finish    10s
    Click Button    id:finish

    Wait Until Location Contains    checkout-complete.html    10s
    Page Should Contain Element     class:complete-header
    Element Text Should Be          class:complete-header    Thank you for your order!

    Log To Console    ✅ Order completed successfully!

    Close Browser