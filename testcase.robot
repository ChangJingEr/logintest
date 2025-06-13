*** Settings ***
Library   SeleniumLibrary

*** Variables ***
#${URL}  https://www.saucedemo.com/
#${BROWSER}  chrome

*** Test Cases ***
TC001 login success
     Open Browser To Login
     Input Information    standard_user    secret_sauce
     Click Login
     Login Title Should Be     Products
     [Teardown]   Close Browser

TC002 empty account
     Open Browser To Login
     Input Information    ${EMPTY}   secret_sauce
     Click Login
     Error Message Should Be    Epic sadface: Username is required
     [Teardown]  Close Browser

TC003 empty secret
     Open Browser To Login
     Input Information    standard_user    ${EMPTY}
     Click Login
     Error Message Should Be  Epic sadface: Password is required
     [Teardown]  Close Browser

TC004 empty empty
     Open Browser To Login
     Input Information    ${EMPTY}    ${EMPTY}
     Click Login
     Error Message Should Be   Epic sadface: Username is required


*** Keywords ***
Open Browser To Login
    Open Browser    https://www.saucedemo.com/     chrome
    Maximize Browser Window

Input Information 
    [Arguments]   ${account}  ${password}
    Input Text   id:user-name  ${account}
    Input Text   id:password   ${password}

Click Login
    Click Button   id:login-button

Login Title Should Be
    [Arguments]  ${expect_title}
    Element Text Should Be    class:title     ${expect_title}

Error Message Should Be 
    [Arguments]  ${expect_message}
    Element Text Should Be   css:[data-test="error"]   ${expect_message}





