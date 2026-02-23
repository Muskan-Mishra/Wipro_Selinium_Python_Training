
#A frame or iframe is an HTML document embedded inside another HTML page.
 #frames will have ids
 #framses will have name
 #frames  will class
 #with indexes
 #0 or 1


*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${url}    https://jqueryui.com/datepicker/

*** Test Cases ***
Verify Sell On Amazon Navigation
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Select Frame    xpath://iframe[@class='demo-frame']
    Sleep    3s
    Click Element    xpath://input[@id='datepicker']
    Sleep    2s
    Click Element    xpath://a[contains(text(),'21')]
    Close All Browsers