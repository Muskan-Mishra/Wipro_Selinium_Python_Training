
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify login with valid credentials
    Log To Console    Enter username
    Log To Console    Enter password
    Log To Console    Click on login button
    Log To Console    User is on the home page