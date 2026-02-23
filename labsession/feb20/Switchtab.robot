
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Screenshot Capture
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # wait for button to be ready
    Wait Until Element Is Visible    id=opentab    10s

    # click the button that opens new window
    Click Element    id=opentab

    # get window handles
    @{windows}=     Get Window Handles
    Log To Console    ${windows}

    @{titles}=      Get Window Titles
    Log To Console    ${titles}

    Switch Window    NEW

    Wait Until Page Contains Element    xpath://h2    10s

    Switch Window    MAIN
    Close Browser