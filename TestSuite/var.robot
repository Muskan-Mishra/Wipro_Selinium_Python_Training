
*** Settings ***
Library    BuiltIn

*** Variables ***
${name}       Deepak
${city}       Patna
${address}    Bihar

@{list1}      apple    mango    banana
@{list2}      10    20    30

&{creds}      username=admin    password=12345

*** Test Cases ***
Verify the variables
    Log    ${name}
    Log    ${city}
    Log    ${address}

    FOR    ${element}    IN    @{list1}
        Log    ${element}
    END

    FOR    ${element}    IN    @{list2}
        Log    ${element}
    END

    Log    ${list1}[0]
    Log    ${list1}[1]

    Log    ${creds}[username]
    Log    ${creds}[password]