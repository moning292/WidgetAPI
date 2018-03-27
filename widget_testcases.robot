*** Settings ***
Library         Collections
Library         WidgetLibrary.py

*** Test Cases ***
Check json file
    Check json
    Result should be    JSON LOAD SUCCESS

#Testsearch
#    &{kwargs}   Create Dictionary    ddd=eeee
#    Testsearch  device  dddd    &{kwargs}
#    Result should be    cccc

Search others all
    #&{kwargs}   Create Dictionary    ddd=eeee
    Search  size  all
    Result should be    Property 'size' is not found 

Search device all
    Search  device  all
    Result should be    ad,news story,image gallery,query,video    

Search device mobile
    Search  device  mobile
    Result should be    ad,news story,query

Search site all
    Search  site    all
    Result should be    ad,news story,image gallery,query,video

Search site perthnow
    Search  site    perthnow
    Result should be    ad,news story,image gallery,query

Search device all capital letter
    Search  DEVICE  ALL
    Result should be    ad,news story,image gallery,query,video

Search device EMPTY
    Search  device  EMPTY
    Result should be    Cannot search

Search EMPTY EMPTY
    Search  EMPTY  EMPTY
    Result should be    Cannot search

Search EMPTY all
    Search  EMPTY  EMPTY
    Result should be    Cannot search

Search special character
    Search  $$%%%%  &&@@@
    Result should be    Invalid character

Search NULL NULL
    Search  NULL    NULL
    Result should be    Search text is none

Search site NULL
    Search  site    NULL
    Result should be    Search text is none

Search NULL all
    Search  NULL    all
    Result should be    Search text is none