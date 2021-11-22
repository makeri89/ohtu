*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  makeri
    Set Password  yliopisto1
    Set Password confirmation  yliopisto1
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  yliopisto1
    Set Password confirmation  yliopisto1
    Submit Credentials
    Registration Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  makeri89
    Set Password  yli
    Set Password confirmation  yli
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  makeri89
    Set Password  yliopisto1
    Set Password confirmation  yliopisto2
    Submit Credentials
    Registration Should Fail With Message  Passwords must match

Login After Successful Registration
    Go To Login Page
    Set Username  makeri
    Set Password  yliopisto1
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username  makeri
    Set Password  password
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Registration Success Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}