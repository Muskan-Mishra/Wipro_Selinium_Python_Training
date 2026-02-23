
rary    SeleniumLibrary

*** Variables ***
${URL}    https://www.tutorialspoint.com/selenium/practice/alerts.php

*** Test Cases ***
Handle Tutorialspoint Alerts
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath:(//button[contains(@class,'btn')])[1]    10s

    # --- SIMPLE ALERT ---
    Click Element    xpath:(//button[contains(@class,'btn')])[1]
    Handle Alert    ACCEPT

    # --- CONFIRM ALERT ---
    Click Element    xpath:(//button[contains(@class,'btn')])[2]
    Handle Alert    DISMISS

    # --- PROMPT ALERT ---
    Click Element    xpath:(//button[contains(@class,'btn')])[3]
    Input Text Into Alert    Hello Priyadarshee

    Close All Browsers