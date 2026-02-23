
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Verify radio buttons
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        #wait till the element
        Wait Until Element Is Visible     xpath://input[@value = 'radio1']
        #click on the radio button
        Click Element    xpath://input[@value = 'radio1']
        #click on check box 3
        Click Element    id=checkBoxOption3

        #close browser
        Close Browser