import re
import urllib.parse as urlparse

class vScans():

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

    def sql_inj_error_based(self,target):
        print(" [!] Trying to initialize SQL injection - Error Based")
        parsed = urlparse.urlparse(target)
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



