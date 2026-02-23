
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Verify multiselect check boxs
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window

       ${elements}=         Get WebElement    xpath://input[@type = 'checkbox]
       FOR    ${element}    IN    @{elements}
           Click Element    ${element}
           Sleep    2s

       END
        #close browser
        Close Browser
