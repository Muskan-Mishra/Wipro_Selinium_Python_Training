
*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections
*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/upload-download.php

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Sleep    3s

    Wait Until Element Is Visible    (//input[@id='uploadFile'])[1]

    Choose File    (//input[@id='uploadFile'])[1]   D:/Downloads/Pytest_MCQs.docx

    Element Text Should Be     xpath://h3[normalize-space()='File Uploaded!']      File Uploaded!

    Sleep    2s


    Close Browser