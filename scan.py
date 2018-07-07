import settings
from scans.vScans import *

def scan_init(scan):
    print(" [!] Scan Initialization started ")
    scanners = vScans()
 
	
    if len(scan) == 1:
        scan_set = scanners.scan_set
    
    if "target" in settings.settings:
        print(" [*] Options")
        for key,value in settings.settings.items():
            print("     - " + str(key) + ": " + str(value))
        
        target = settings.settings["target"]
        for scan in scan_set:
            scan_set[scan](target)
    else:
        print(" [!] Scan stopped: Target is not set")