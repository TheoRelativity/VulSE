import re
import injector

def error_based_sqli_func():
    print(" [!] Now Scanning for Error Based SQL Injection ")
    print(" [!] Covering MySQL, Oracle, MSSQL, MSACCESS & PostGreSQL Databases ")
    print(" [!] Please wait ....")
    
    payloads = {
	 0: ["'","' or 1=1--","HIGH","Tautology Injection"]
	 }
    check = re.compile("Error: You have an error in your SQL syntax|Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
    injector.injector(payloads, check)