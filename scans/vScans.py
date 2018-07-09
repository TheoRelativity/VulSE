import re
from lib.vRequests import *
import urllib.parse as urlparse

class vScans(object):

    def __init__(self):
        
        self.scanners = {
		    "full": {
			          0: self.sql_inj_error_based
			    },
				
			"sql_inj": {
			    "full": {
				      0: self.sql_inj_error_based
			      },
				"error_based": {
				      0: self.sql_inj_error_based
				}
			}
		}
        
        self.scan_set =  self.scanners["full"]
        
        self.vRequests = vRequests()

    def sql_inj_error_based(self,target):
        payloads = {
		    # ATTACK, Don't execute it if you already performed one of attack in the list
            0: ["'"],
			1: ['"', [0]],
			2: [";"]
        }
        error_list = re.compile("Error: You have an error in your SQL syntax|Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
        print(" [!] Trying to initialize SQL injection - Error Based")
        parsed = urlparse.urlparse(target)
        if urlparse.parse_qs(parsed.query) == None:
            print(" [!] The target has no params.")
            print(" [!] SQL Injection scan can't be executed")
            return(0)
        print(" [!] SQL Injection initialized correctly")
        print("\n Now Scanning for SQL Injection - Error Based")
     
		
        for params in target.split("?")[1].split("&"):
            print(" [!] Testing param: " + str(params))
            for key,payload in payloads.items():
                sql_inj_url = target.replace(params, params + str(payload[0]).strip())
                attack_result = self.vRequests.custom(sql_inj_url)
                for line in attack_result["text"].splitlines():
                    checker = re.findall(error_list, str(line))
                    if len(checker) !=0:
                        print(" [*] Payload Found . . .")
                        print(" [!] Code Snippet: "  + str(line).strip())

        print(" [!] Please wait ....")





class xssInjection(vScans):
    
    def __init__(self):
        vScans.__init__()
        i = len(vScans.scanners["full"])
        vScans.scanners["full"][i] = self.xss_inj_error_based
        vScans.scanners["xss_inj"] = { 
		                                "full": {
                                              0: self.sql_inj_error_based
			                                    },
				                        "error_based": {
				                              0: self.sql_inj_error_based
				                                }
			                          }

    def xss_inj_error_based(self):
        print(vScans.scanners["full"])
        print(" [!] XSS Inj started")
         
# vScans = vScans()

# vScans.sql_inj_error_based('http://localhost')
    
# xssInj = xssInjection()

# xssInj.xss_inj_error_based()



