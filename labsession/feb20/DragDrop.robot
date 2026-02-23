
*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Verify Drag And Drop In Droppable Page
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Sleep    3s

    Wait Until Element Is Visible    (//div[@id='draggable'])[1]
    Sleep    2s

    Drag And Drop    (//div[@id='draggable'])[1]    (//div[@id='droppable'])[1]
    Sleep    2s

    Close Browser