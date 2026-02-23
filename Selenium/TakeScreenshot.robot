

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload
${path}   D:/Downloads

*** Test Cases ***
Verify Screenshot Capture
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@id='file-upload']

    # capture full page screenshot
    Capture Page Screenshot    ${path}/Robo5.jpg

    # capture element screenshot
    Capture Element Screenshot    xpath://input[@id='file-upload']    ${path}/Robo6.jpg

    Sleep    2s
    Close Browser