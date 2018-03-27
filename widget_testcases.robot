*** Settings ***
Library         Collections
Library         WidgetLibrary.py

*** Test Cases ***
#Test cases ID can be mapped with the test matrix table in README.md
TC1 Search device mobile
    Search  device  mobile
    Result should be    ad,news story,query

TC2 Search device desktop
    Search  device  desktop
    Result should be    news story,image gallery,query,video

TC3 Search device all
    Search  device  all
    Result should be    ad,news story,image gallery,query,video

TC4 Search site perthnow
    Search  site    perthnow
    Result should be    ad,news story,image gallery,query

TC5 Search site dailytelegraph
    Search  site    dailytelegraph
    Result should be    ad,news story,image gallery,video

TC6 Search site theaustralian
    Search  site    theaustralian
    Result should be    ad,news story,query,video    

TC7 Search site all
    Search  site    all
    Result should be    ad,news story,image gallery,query,video

#Invalid scenarios
Check json file
    Check json
    Result should be    JSON LOAD SUCCESS

Search others all
    Search  size  all
    Result should be    Property 'size' is not found 

Search device all capital letter
    Search  DEVICE  ALL
    Result should be    ad,news story,image gallery,query,video

Search word with whitespace
    Search  mobile phone    all
    Result should be    Property 'mobile phone' is not found    

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
    Search  s$%%%%  a@@@
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

#incomplete - can search device only
Search with filters
    &{kwargs}   Create Dictionary    device=desktop     device=desktop
    Search with filters  &{kwargs}
    Result should be    news story,image gallery,query,video