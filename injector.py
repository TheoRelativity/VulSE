import urllib.request
import re
from tests import *
import settings
from lib.vRequests import *


def injector_init(attacks):
    tests = {
	 0: error_based_sqli_func
	}
    print(" [!] Detecting configurations")
    if "target" in settings.settings:
        print(" [*] Options")
        for key,value in settings.settings.items():
            print("     - " + str(key) + ": " + str(value))
        for attack in attacks:
            tests[attack]()
    else:
        print(" [!] Target is not set")


def injector(payloads, check):
    vulser = vRequests()
    vulser.custom(settings.settings["target"])
	
	# This code flow must be ignored.
    print(" [!] Injector started")
    vulnerabilities = 0
    target_url = settings.settings["target"]

    for params in target_url.split("?")[1].split("&"):
        print(" [!] Testing param: " + str(params))
		
        for key,payload in payloads.items():
            # Use a proxy
            if "proxy" in settings.settings and settings.settings["proxy"] != "off":
                proxy = urllib.request.ProxyHandler({'http': settings.settings["proxy"]})
                opener = urllib.request.build_opener(proxy)
                urllib.request.install_opener(opener)
            
           		
            injected_url = target_url.replace(params, params + str(payload[0]).strip())
            inj_req = urllib.request.Request(injected_url)
            try:
                inject = urllib.request.urlopen(injected_url)
            except urllib.error.HTTPError as e:		                
                print(" [!] Error. Exit code " + str(e.code()))
                main()
            with inject as inj_response:
                if inj_response.code == 200:
                    inj_html = inj_response.read()
                    print(" [*] Inj_Page response code " + str(inj_response.code))
                    for line in inj_html.splitlines():
                        checker = re.findall(check, str(line))
                        if len(checker) !=0:
                            print(" [*] Payload Found . . .")
                            print(" [*] Payload: " + str(payload))
                            #print(" [!] Code Snippet: "  + str(line).strip())
                            vulnerabilities+=1
            inject.close()
    if vulnerabilities == 0:                
        print(" [!] Target is not vulnerable!")
    else:
        print(" [!] Congratulations you've found %i bugs :-) " % (vulnerabilities) )
