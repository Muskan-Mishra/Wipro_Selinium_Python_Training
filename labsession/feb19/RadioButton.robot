
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${URL}      https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify Checkbox Selection
    # Open the browser
    Open Browser    ${URL}    chrome

    # Wait for child checkbox to appear
    Wait Until Element Is Visible    xpath://input[@id='c_bs_1']    20s

    # Click checkbox "Main Level 1"
    Click Element    xpath://input[@id='c_bs_1']
    Sleep       2s

    # Close browser
    Close Browser