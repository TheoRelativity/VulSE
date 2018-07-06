# settings.py

def init():
    global settings
    settings = {
	    "proxy":       "on",
	    "http-proxy":  "127.0.0.1:8080",
		"https-proxy": "",
		"user-agent":  "VulSE 0.0",
		"cookies":     {},
		"auth":1
		
		}
	
def print_error(error_code):
    errors = {
	0: " [!] Missing arguments",
	1: " [!] Unknown parameter"
	}
    return print(errors[error_code])