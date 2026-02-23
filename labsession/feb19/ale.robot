
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://rahulshettyacademy.com/AutomationPractice/
${NAME}   Priyadarshee

*** Test Cases ***
Handle Rahul Shetty Alerts
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Scroll Element Into View    id:alertbtn

    Input Text    id:name    ${NAME}

    Click Button    id:alertbtn
    ${text}=    Handle Alert    ACCEPT
    Log To Console    Alert Text: ${text}

    Click Button    id:confirmbtn
    ${confirm_text}=    Handle Alert    DISMISS
    Log To Console    Confirm Text: ${confirm_text}

    Close All Browsers