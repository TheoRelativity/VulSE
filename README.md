# VulSE

VulSE is a Python application which searches for vulnerabilities into a web application, network, web server. Currently is still a work in progress. I am a PHP developer who is studying to become a certified ethical hacker and I am developing this application to study web applications, web servers, networks vulnerabilities and Python.  

**This project is a work in progress.**

> Latest update 09 July 2018

```bash
    ______
   /_____/\__  __  _____   _____
   \__  _\/_/_/_/\/____/\ /____/\
      \ \ \ \-\ \/_   _\//     \/
      R  e  l  a  t  i_ v  i  t  Y
         \_\/\_\/\_\/\\__//\___//

     github.com/TheoRelativity/VulSE

                VulSE 0.3
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

**Currently not active - 0.2**
```bash
vulse: set proxy 127.0.0.1:8080
```

## Scanner Example

The simplest scanner is the "SQL Injection scanner - Error Based". The scanner sends a payload to the target and then analyze the result of the attack.
Example. 

Target: averybuggedsite.com/vulnerable_page.php?select_user=12

parameter: 12

payload: parameter'

Once the injection has been executed by the scanner, it analyzes the response of the request and it searches for SQL/Database/DBMS error strings.

## Changelog

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
