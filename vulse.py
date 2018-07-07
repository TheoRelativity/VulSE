from lib.vRequests import * 
import settings
from scan import *
settings.init()

print('''   
    ______   
   /_____/\\__  __  _____   _____
   \__  _\/_/_/_/\\/____/\\ /____/\\
      \ \ \\ \-\\ \\/_   _\\//     \/
      R  e  l  a  t  i_ v  i  t  Y
         \\_\\/\\_\\/\\_\/\\\\__//\\___//

     github.com/TheoRelativity/VulSE
	 
                VulSE 0.1
       Vulnerabilities Search Engine
        
         It is a work in progress.

''')

def commands(user_commands):
    if len(user_commands) > 0:
        if user_commands[0] == "show":
            show(user_commands)
        elif user_commands[0] == "set":
            set(user_commands)
        elif user_commands[0] == "exit":
            exit()
        elif user_commands[0] == "scan":
            scan_init(user_commands)
            main()
    elif user_commands[0] == "scan":
        scan_init(user_commands)
    else:
        print(" [!] Unknown command")
        main()


def set(user_commands):
     total_words = len(user_commands)
     if  total_words > 2:
        if user_commands[1] == "cookie":
            settings.settings['cookies'][user_commands[2]] = user_commands[3]
            print(" [*] Cookies set: " + str(settings.settings["cookies"]))
            main()
        if user_commands[1] == "proxy": 
            settings.settings['proxy'] = "on" if user_commands[2] == "on" else "off"
            print(" [*] Proxy ok: " + settings.settings["proxy"])
            main()
        if user_commands[1] == "target":
            settings.settings['target'] = user_commands[2]
            print("\n [*] Target set: " + settings.settings["target"] + "\n")
            main()
        if user_commands[1] == "auth":
            settings.settings['auth'] = user_commands[2]
            print(" [*] Auth set: " + str(settings.settings["auth"]))
            main()
        else:
            settings.print_error(1)
            main()
     else:
         print(" [!] You are missing required parameters")
         main()

def show(user_commands):
     total_words = len(user_commands)
     if  total_words > 1:
        if user_commands[1] == "config":
            print("\n========= C O N F I G =========\n")
            for key,value in settings.settings.items():
                print("   " + str(key) + ": " + str(value))
            print("\n===============================\n")
     main()
	 
def main():
    user_input = input("vulse:")
    user_commands = user_input.split()
    commands(user_commands)

def start(tests=0):
    if tests == 0:
        print(" [*] Full test selected")
        injector_init([0])
        print(" [!] Test ended with success")
        main()

main()

