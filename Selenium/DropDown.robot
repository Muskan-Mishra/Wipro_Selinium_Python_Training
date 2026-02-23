
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Drop downs
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Wait Until Element Is Visible    id=dropdown-class-example

    # Get default selected value
    ${labels}=    Get Selected List Labels    id=dropdown-class-example
    Log    ${labels}

    # Selecting by visible text (Label)
    Select From List By Label    id=dropdown-class-example    Option3
    Sleep    2s

    # Selecting by index (starts from 0)
    Select From List By Index    id=dropdown-class-example    2
    Sleep    2s

    # Selecting by value attribute
    Select From List By Value    id=dropdown-class-example    option1
    Sleep    2s

    Close Browser