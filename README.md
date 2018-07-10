# VulSE

VulSE is a Python application which searches for vulnerabilities into a web application, network, web server. Currently is still a work in progress. I am a PHP developer who is studying to become a certified ethical hacker and I am developing this application to study web applications, web servers, networks vulnerabilities and Python.  

**This project is a work in progress.**

> Latest update 10 July 2018

```bash
    ______
   /_____/\__  __  _____   _____
   \__  _\/_/_/_/\/____/\ /____/\
      \ \ \ \-\ \/_   _\//     \/
      R  e  l  a  t  i_ v  i  t  Y
         \_\/\_\/\_\/\\__//\___//

     github.com/TheoRelativity/VulSE

                VulSE 0.4
       Vulnerabilities Search Engine

    This project is a work in progress.

```

## What it does?

It scans a target (web page, web server) and tries to detect vulnerabilities and generates a detailed report[1]. Its scanners can be added at runtime execution.[1] This feature permits to every developer to implement its own scanner to add to the application.

[1] Feature under development

## Installation

### Requirements
- Python3
- [Requests](https://github.com/requests/requests/) Library installed

## How it works?

Once launched vulse.py in a shell/cmd

You have to set up a target.

```bash

vulse: set target http://vulnerablesite.com/buggedpage.php?title=c&action=search
[*] Target set: http://vulnerablesite.com/buggedpage.php?title=c&action=search

```
# Start a scan

```bash
vulse: scan
```
## Parameters

Currently is available only the full-scan feature. 

## Using Cookies

```bash
set cookie PHPSESSID 1a5s6d1as65d4564sdq
```
## Show Config

```bash
show config
```

## Using a Proxy

```bash
set proxy on
```

**Currently not active -   >0.2**

```bash
vulse: set proxy 127.0.0.1:8080
```

## Set Method GET/POST

```bash
set method post
```
### Set Data for POST requests

```bash
set data ?title=text&action=search
```

## Plugins

**Note** the feature "set in" has been implemented in the 0.4 version but will be completed in the version 0.5

### SQL Injection Error Based

Description: It searches for SQL injection vulnerabilities analyzing the results of the attack.

id: sql_inj_eb

### Features

#### Filters Detection

parameters: 
 * check_text: Use this text to detect filters
 
### Example of usage

```bash
vulse: set target http://localhost/vulnerables/bwapp/sqli_1.php?title=ciao&action=search
[*] Target set: http://localhost/vulnerables/bwapp/sqli_1.php?title=&action=search
vulse: set in sql_inj_eb check_text "No movies were found!"
[*] Plugin settings updated: {'check_text': 'No movies were found!'}
vulse:scan
 [!] Scan Initialization started
 [*] Options
     - proxy: on
     - http-proxy: 127.0.0.1:8080
     - https-proxy:
     - user-agent: VulSE 0.0
     - cookies: {'security_level': '1', 'PHPSESSID': 'qiud7u5kgbe59po7hbuds6k5i6
'}
     - method: get
     - data:
     - scan: full
     - target: http://localhost/vulnerables/bwapp/sqli_1.php?title=ciao&action=search

                #####################################
                #                                   #
                # SQL injection - Error Based v. 0  #
                #                                   #
                #####################################

 [!] SQL Inj EB initialized correctly
 [!] Testing param: title=ciao
 [*] Filter Detected!!!
 [*] Filter Detected!!!
 [!] Testing param: action=search
 [*] Filter Detected!!!
 [*] Filter Detected!!!
 [!] Scan complete
```


## Changelog

### 0.4
10 July 2018

- Added a draft of sql_inj_error_based plugin
- Implemented the plugin's idea
- Added POST request in vRequest.custom()
- Added plugin settings
- Added "set in" feature

### 0.3
09 July 2018

- Added dict results in vResults.custom() for easy management
- Implemented the draft method sql_inj_error_based in vScans

### 0.2
08 July 2018

- Modular structure added 
- tests.py file deprecated
- vSearch class added
- scan.py file added
- start feature deprecated
- scan feature added

### 0.1
07 July 2018

- Added [Requests](https://github.com/requests/requests/): HTTP for Humans
- Created vRequests class to manage Requests library
- Added user-agent
- Added set cookie feature
- Added turn on/off proxy
- Added show config feature
