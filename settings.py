# settings.py

def init():
    global settings
    global plugins
    plugins = {}
    settings = {
	    "proxy":       "on",
	    "http-proxy":  "127.0.0.1:8080",
		"https-proxy": "",
		"user-agent":  "VulSE 0.0",
		"cookies":     {"security_level":"1","PHPSESSID":"qiud7u5kgbe59po7hbuds6k5i6"},
		"method":      "get",
		"data":        "",
		"scan":        "full"
		}
	
def print_error(error_code):
    errors = {
	0: " [!] Missing arguments",
	1: " [!] Unknown parameter"
	}
    return print(errors[error_code])