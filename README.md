# VulSE
VulSE is a Py application which searches for vulnerabilities into a web page. I developed it to learn how to code in Python.

**This project is still under developing.**

```bash
    ______
   /_____/\__  __  _____   _____
   \__  _\/_/_/_/\/____/\ /____/\
      \ \ \ \-\ \/_   _\//     \/
      r  e  l  a  t  i_ v  i  t  y
         \_\/\_\/\_\/\\__//\___//

     github.com/TheoRelativity/VulSE

                VulSE 0.0
       Vulnerabilities Search Engine

    This project is still under developing.

```

## What it does?

He tries to hack a webpage using preloaded attacks on it and then analyzes results to determine if is vulnerable.

## How it works?

Once launched vulse.py in a shell/cmd

You have to set up a target.

```bash

vulse: set target http://vulnerablesite.com/buggedpage.php?title=c&action=search
[*] Target set: http://vulnerablesite.com/buggedpage.php?title=c&action=search
vulse: start

```
**Note** You have to use a link with parameters.

 
## Using a Proxy


```bash
vulse: set proxy 127.0.0.1:8080
```
