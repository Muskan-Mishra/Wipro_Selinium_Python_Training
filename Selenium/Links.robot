
*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify links
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    @{links}=         Get WebElements    xpath://a
    FOR    ${link}    IN    @{links}
        ${text}=        Get Text    ${link}
        ${url}=         Get Element Attribute    ${link}    href
        Log To Console    ${text}
        Log To Console    ${url}

    END
    Close All Browsers