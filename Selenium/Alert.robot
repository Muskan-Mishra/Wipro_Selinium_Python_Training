
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Verify JavaScript Alerts
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath:(//button)[1]    5s
    Click Element    xpath:(//button)[1]
    Handle Alert    ACCEPT    10s

    Click Element    xpath:(//button)[2]
    Handle Alert    DISMISS    10s

    Click Element    xpath:(//button)[3]
    Input Text Into Alert    Hello Priyadarshee

    Close Browser