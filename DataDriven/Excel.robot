
*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    C:/Users/MUSKAN MISHRA/Downloads/ddtLogindata.xlsx    sheet_name=ddtLogindata
Test Template     Login Test
Test Setup        Open Browser To Login Page
Test Teardown     Close Browser

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}        firefox

*** Test Cases ***
Login with User    ${username}    ${password}

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    xpath://input[@name="username"]    10s
    Input Text    xpath://input[@name="username"]    ${username}
    Input Text    xpath://input[@name="password"]    ${password}
    Click Button    xpath://button[@type="submit"]