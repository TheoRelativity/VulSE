import re
import injector
import urllib.parse as urlparse
import settings

def sql_inj_error_based():
    print(" [!] Trying to initialize SQL injection - Error Based")
    parsed = urlparse.urlparse(settings.settings["target"])
    if urlparse.parse_qs(parsed.query) == None:
        print(" [!] The target has no params.")
        print(" [!] SQL Injection scan can't be executed")
        return(0)
    print(" [!] Now Scanning for SQL Injection - Error Based")
    print(" [!] Please wait ....")
    payloads = {
	 0: ["'","' or 1=1--","HIGH","Tautology Injection"]
	 }
    check = re.compile("Error: You have an error in your SQL syntax|Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
    print(" [!] SQL Injection initialized correctly")