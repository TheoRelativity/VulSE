# settings.py

def init():
    global settings
    settings = {}
	
def print_error(error_code):
    errors = {
	0: " [!] Missing arguments",
	1: " [!] Unknown parameter"
	}
    return print(errors[error_code])