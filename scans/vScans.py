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
        print('''
		##################################### 
		#                                   #
		# SQL injection - Error Based v. 0  #
		#                                   #
		#####################################\n ''')
        settings.plugins["sql_inj_eb"] = { 
					"check_text": "The movie does not exist in our database!"
				 }

        payloads = {
		    # ATTACK, Don't execute it if you already performed one of attack in the list
            0: ["'"],
			2: [";"]
        }
        error_list = re.compile("Error: You have an error in your SQL syntax", re.I)
        vulnerabilities = { 
		                    "total": 0,
							"list": []
		                  }
        method = "get" #default get
		
		# Detecting POST method 
        if settings.settings["method"] == "post":
            if len(settings.settings["data"]) ==0:
                print(" [!] Missind data for post method")
                return()
            else:
                method = "post"
				 
        # GET method
        if method == "get":
            parsed = urlparse.urlparse(target)
            if len(urlparse.parse_qs(parsed.query,keep_blank_values=True)) == 0:
                print(" [!] The target has no params.")
                print(" [!] SQL Injection scan can't be executed")
                return(0)
				
            print(" [!] SQL Inj EB initialized correctly")
            
            for params in target.split("?")[1].split("&"):
                print(" [!] Testing param: " + str(params))
                for key,payload in payloads.items():
                    sql_inj_url = target.replace(params, params + str(payload[0]).strip())
                    attack_result = self.vRequests.custom(sql_inj_url)
					
					# Use the check_text to detect filters
                    if settings.plugins["sql_inj_eb"]["check_text"] != "":
                        checker = re.findall(settings.plugins["sql_inj_eb"]["check_text"], attack_result["text"])
                        if len(checker) !=0:
                            print(" [*] Filter Detected!!!")
                         
                    for line in attack_result["text"].splitlines():
                        checker = re.findall(error_list, str(line))
                        if len(checker) !=0:
                            print(" [*] Payload Found . . .")
                            vulnerabilities["total"]+=1
                            vulnerabilities["list"].append(payload[0])
                        
        if method == "post":
            data = settings.settings["data"]
            print(" [!] SQL Inj EB initialized correctly")
            for params in data.split("?")[1].split("&"):
                print(" [!] Testing param: " + str(params))
                for key,payload in payloads.items():
                    inj_data = data.replace(params, params + str(payload[0]).strip())
                    attack_result = self.vRequests.custom(target,{"data":inj_data,"method":"post"})
                    for line in attack_result["text"].splitlines():
                        checker = re.findall(error_list, str(line))
                        if len(checker) !=0:
                            print(" [*] Payload Found . . .")

        print(" [!] Scan complete")



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



