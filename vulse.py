import settings
from injector import *
settings.init()

print('''   
    ______   
   /_____/\\__  __  _____   _____
   \__  _\/_/_/_/\\/____/\\ /____/\\
      \ \ \\ \-\\ \\/_   _\\//     \/
      r  e  l  a  t  i_ v  i  t  y
         \\_\\/\\_\\/\\_\/\\\\__//\\___//

     github.com/TheoRelativity/VulSE
	 
                VulSE 0.0
       Vulnerabilities Search Engine
        
    This project is still under developing.

''')

def commands(user_commands):
    if len(user_commands) > 0:
        if user_commands[0] == "set":
            set(user_commands)
        if user_commands[0] == "start":
            if len(user_commands) == 1:
                start()
        elif user_commands[0] == "exit":
            exit()
        else:
            print(" [!] Unknown command")
            main()


def set(user_commands):
     total_words = len(user_commands)
     if  total_words > 2:
        if user_commands[1] == "proxy":
            settings.settings['proxy'] = user_commands[2]
            print(" [*] Proxy ok: " + settings.settings["proxy"])
            main()
        if user_commands[1] == "target":
            settings.settings['target'] = user_commands[2]
            print(" [*] Target set: " + settings.settings["target"])
            main()
        else:
            settings.print_error(1)
            main()
     else:
         print(" [!] You are missing required parameters")
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

