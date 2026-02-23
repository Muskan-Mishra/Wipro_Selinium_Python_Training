
*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Sleep    3s

    Wait Until Element Is Visible    xpath://a[normalize-space()='Sell']
    Open Context Menu    xpath://a[normalize-space()='Sell']
    Sleep    2s

    # double click
    Double Click Element    xpath://a[normalize-space()='Mobiles']
    Sleep    2s

    Close Browser