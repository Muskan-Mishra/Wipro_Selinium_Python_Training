
*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify Sell On Amazon Navigation
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Page Contains Element    xpath://a[contains(.,'Sell on Amazon')]    15s

    Wait Until Element Is Visible    xpath://a[contains(.,'Sell on Amazon')]    10s
    Click Element    xpath://a[contains(.,'Sell on Amazon')]

    Close All Browsers