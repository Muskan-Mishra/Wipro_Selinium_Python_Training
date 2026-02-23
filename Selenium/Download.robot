
*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL}        https://the-internet.herokuapp.com/download
${FILE}       upload.txt
${DOWNLOADS}  D:/Downloads

*** Test Cases ***
Download File
    # Set Chrome preferences for automatic download
    &{prefs}=    Create Dictionary    download.default_directory=${DOWNLOADS}    profile.default_content_settings.popups=0
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_experimental_option    prefs    ${prefs}

    # Open Browser with options
    Open Browser    ${URL}    chrome    options=${options}

    # Wait until the link is visible and click
    Wait Until Element Is Visible    xpath=//a[text()='${FILE}']    10s
    Click Element    xpath=//a[text()='${FILE}']

    # Wait until file exists
    Wait Until Keyword Succeeds    20x    1s    File Should Exist    ${DOWNLOADS}/${FILE}

    Close Browser