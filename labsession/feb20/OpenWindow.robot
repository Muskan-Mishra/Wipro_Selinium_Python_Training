
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Screenshot Capture
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Wait Until Element Is Visible    id=openwindow    10s
    Click Element    id=openwindow

    @{windows}=     Get Window Handles
    Log To Console    ${windows}

    @{titles}=      Get Window Titles
    Log To Console    ${titles}

    Switch Window    NEW

    # validate content in new window
    Wait Until Page Contains Element    xpath://h2    10s

    Switch Window    MAIN
    Close Browser