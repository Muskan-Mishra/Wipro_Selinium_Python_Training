
*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Banking App
Suite Teardown    Close Browser
Test Setup        Go To Login Page

*** Variables ***
${LOGIN_URL}      https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
${BROWSER}        Chrome
${DEPOSIT_AMT}    100
${WITHDRAW_AMT}   50
${LONG_WAIT}      20s

*** Keywords ***
Open Browser To Banking App
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    css=button[ng-click="manager()"]    timeout=${LONG_WAIT}
    Wait Until Element Is Visible    css=button[ng-click="customer()"]    timeout=${LONG_WAIT}

Go To Login Page
    Go To    ${LOGIN_URL}
    Wait Until Element Is Visible    css=button[ng-click="manager()"]    timeout=${LONG_WAIT}

Login As Bank Manager
    Click Button    css=button[ng-click="manager()"]
    Wait Until Element Is Visible    css=button[ng-click="addCust()"]    timeout=${LONG_WAIT}

Login As Customer
    Click Button    css=button[ng-click="customer()"]
    Wait Until Element Is Visible    css=select[ng-model="custId"]    timeout=${LONG_WAIT}
    Select From List By Label    css=select[ng-model="custId"]    John Doe
    Click Button    css=button[type="submit"]
    # Wait for Deposit button instead of Logout (AngularJS rendering)
    Wait Until Element Is Visible    css=button[ng-click="deposit()"]    timeout=${LONG_WAIT}

Add Customer
    Login As Bank Manager
    Click Button    css=button[ng-click="addCust()"]
    Wait Until Element Is Visible    css=input[ng-model="fName"]    timeout=${LONG_WAIT}
    Input Text      css=input[ng-model="fName"]    John
    Input Text      css=input[ng-model="lName"]    Doe
    Input Text      css=input[ng-model="postCd"]    560001
    Click Button    css=button[type="submit"]
    Handle Alert    action=ACCEPT
    Sleep    1s    # allow Angular to update customer list

Open Customer Account
    Login As Bank Manager
    Click Button    css=button[ng-click="openAccount()"]
    Wait Until Element Is Visible    css=select[ng-model="custId"]    timeout=${LONG_WAIT}
    Select From List By Label    css=select[ng-model="custId"]    John Doe
    Select From List By Label    css=select[ng-model="currency"]    Dollar
    Click Button    css=button[type="submit"]
    Handle Alert    action=ACCEPT
    Sleep    1s

Deposit Money
    [Arguments]    ${amount}
    Click Button    css=button[ng-click="deposit()"]
    Wait Until Element Is Visible    css=input[ng-model="amount"]    timeout=${LONG_WAIT}
    Input Text      css=input[ng-model="amount"]    ${amount}
    Click Button    css=button[type="submit"]
    Page Should Contain    Deposit Successful

Withdraw Money
    [Arguments]    ${amount}
    Click Button    css=button[ng-click="withdrawl()"]
    Wait Until Element Is Visible    css=input[ng-model="amount"]    timeout=${LONG_WAIT}
    Input Text      css=input[ng-model="amount"]    ${amount}
    Click Button    css=button[type="submit"]
    Page Should Contain    Transaction successful

Get Balance
    ${balance_text}=    Get Text    css=strong[class="ng-binding"]
    ${balance}=         Convert To Integer    ${balance_text}
    RETURN            ${balance}

*** Test Cases ***
TC00 Open App & Validate Home
    Wait Until Page Contains    XYZ Bank    timeout=${LONG_WAIT}

TC01 Add Customer
    Add Customer

TC02 Open Account
    Open Customer Account

TC03 Customer Deposit & Withdraw
    Login As Customer
    ${balance1}=    Get Balance
    Log    Initial balance = ${balance1}

    Deposit Money    ${DEPOSIT_AMT}
    ${balance2}=    Get Balance
    ${expected_balance2}=    Evaluate    ${balance1} + ${DEPOSIT_AMT}
    Should Be Equal As Integers    ${balance2}    ${expected_balance2}

    Withdraw Money   ${WITHDRAW_AMT}
    ${balance3}=    Get Balance
    ${expected_balance3}=    Evaluate    ${balance2} - ${WITHDRAW_AMT}
    Should Be Equal As Integers    ${balance3}    ${expected_balance3}

TC04 Validate Balance End‑to‑End
    Login As Customer
    ${finalBalance}=    Get Balance
    Log    Final balance is ${finalBalance}