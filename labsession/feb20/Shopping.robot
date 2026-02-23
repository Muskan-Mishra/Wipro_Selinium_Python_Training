
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://practice.automationtesting.in/
${BROWSER}    chrome

*** Test Cases ***
Add Item To Cart And Checkout
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    Click Element    xpath://a[text()='Shop']

    Click Element    xpath://body

    Scroll Element Into View    xpath:(//a[text()='Add to basket'])[1]
    Click Element               xpath:(//a[text()='Add to basket'])[1]

    Wait Until Element Is Visible    xpath://a[@title='View your shopping cart']    15s

    Click Element    xpath://a[@title='View your shopping cart']

    Element Should Be Visible    xpath://a[contains(@class,'remove')]

    Wait Until Element Is Visible    xpath://a[normalize-space(text())='Proceed to Checkout']    15s
    Scroll Element Into View         xpath://a[normalize-space(text())='Proceed to Checkout']
    Click Element                    xpath://a[normalize-space(text())='Proceed to Checkout']

    Wait Until Element Is Visible    xpath://h3[text()='Billing Details']    10s
    Element Should Be Visible        xpath://h3[text()='Billing Details']

    Close Browser