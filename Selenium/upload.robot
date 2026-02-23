
*** Settings ***
Library    SeleniumLibrary
Library OperatingSystem
Library Collections

*** Variables ***
${url}       https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify Checkboxes
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep 3s
    Wait Until Element Is visible       xpath://input[@id='file-upload']
    Choose File     xpath://input[@id='file-upload]         C:\Users\MUSKAN MISHRA\OneDrive\Documents
    Click Element         xpath://input[@id='file-submit']
    Element Text Should Be          xpath://h3[normalize-space()='File Uploaded!']      File Uploaded!
    Close Browser