*** Settings ***
Library                 WidgetLibrary.py

*** Test Cases ***
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