*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  makeri  yliopisto1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  makeri  yliopisto1
    Input New Command
    Input Credentials  makeri  yliopisto2
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ma  yliopisto1
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  makeri  yliopi
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  makeri  yliopisto
    Output Should Contain  Password can not contain only letters
