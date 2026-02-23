
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/windows

*** Test Cases ***
Verify Screenshot Capture
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    Click Element    link=Click Here
    @{windows}=     Get Window Handles
    Log To Console    ${windows}
    @{titles}=      Get Window Titles
    Log To Console    ${titles}

    Switch Window       title=New Window
    Element Text Should Be    xpath://h3[contains(text(),'New Window')]    New Window

    Switch Window       MAIN
    Close Browser