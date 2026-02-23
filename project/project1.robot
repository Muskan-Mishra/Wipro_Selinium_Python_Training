

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome
${USERNAME}  Admin
${PASSWORD}  admin123

*** Keywords ***

Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@name="username"]    20s

Login
    Input Text    xpath=//input[@name="username"]    ${USERNAME}
    Input Text    xpath=//input[@name="password"]    ${PASSWORD}
    Click Element    xpath=//button[@type="submit"]
    Wait Until Element Is Visible    xpath=//span[text()="Admin"]    20s

Go To My Info
    Click Element    xpath=//span[text()="My Info"]
    Wait Until Element Is Visible    xpath=//input[@name="firstName"]    20s

Safe Save
    Wait Until Element Is Not Visible    xpath=//div[contains(@class,"oxd-form-loader")]    20s
    Click Element    xpath=(//button[@type="submit"])[1]
    Wait Until Element Is Not Visible    xpath=//div[contains(@class,"oxd-form-loader")]    20s

Logout
    Click Element    xpath=//p[@class="oxd-userdropdown-name"]
    Click Element    xpath=//a[text()="Logout"]
    Wait Until Element Is Visible    xpath=//input[@name="username"]    20s

Close
    Close Browser


*** Test Cases ***

TC_01 Verify Successful Login
    Open Login Page
    Login
    Logout
    Close

TC_02 Verify Unsuccessful Login
    Open Login Page
    Input Text    xpath=//input[@name="username"]    wrong
    Input Text    xpath=//input[@name="password"]    wrong
    Click Element    xpath=//button[@type="submit"]
    Wait Until Element Is Visible    xpath=//p[contains(@class,"alert-content-text")]    20s
    Close

TC_03 Modify First Name Successfully
    Open Login Page
    Login
    Go To My Info
    Clear Element Text    xpath=//input[@name="firstName"]
    Input Text    xpath=//input[@name="firstName"]    Muskan
    Safe Save
    Logout
    Close

TC_04 Negative Test - Invalid First Name
    Open Login Page
    Login
    Go To My Info
    Clear Element Text    xpath=//input[@name="firstName"]
    Input Text    xpath=//input[@name="firstName"]    12345
    Safe Save
    Logout
    Close