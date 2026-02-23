
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify login with valid credentials
    Log    Enter username
    Log    Enter password
    Log    Click on login button
    Log    User is on the home page