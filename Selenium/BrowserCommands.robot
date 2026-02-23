
*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections
*** Variables ***
${url}      https://the-internet.herokuapp.com/

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Go Back
    Sleep    3s
    Go To    ${url}
    Sleep    2s
    Reload Page
    Sleep    2s


    Close Browser
