
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${URL}      https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Select State And City
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    # Wait until State dropdown is visible
    Wait Until Element Is Visible    id=state    10s

    # Select Uttar Pradesh
    Select From List By Label    id=state    Uttar Pradesh
    Sleep    2s

    # Wait until City dropdown is ready
    Wait Until Element Is Visible    id=city    10s

    # Select "Lucknow" from City dropdown
    Select From List By Label    id=city    Lucknow
    Sleep    2s

    Close Browser