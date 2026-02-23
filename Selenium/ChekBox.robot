
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify Checkboxes
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Wait Until Page Contains Element    xpath://input[@type='checkbox']    10s

    ${elements}=    Get WebElements    xpath://input[@type='checkbox']

    FOR    ${element}    IN    @{elements}
        Scroll Element Into View    ${element}
        Select Checkbox    ${element}
        Sleep    1s
    END

    Sleep    2s
    Close Browser