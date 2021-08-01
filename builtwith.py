def builtwith():
        import os
        import time
        import sys
        import builtwith
        from baner import baner
        from colorama import Fore
        os.system("clear")
        baner()
        time.sleep(1)
        target =  input(Fore.RED+" ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Builtwith"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
        if target == "" or None or len(target) <= 1:
            print(Fore.RED + "\n[!] ~ Error : Your Input Is Not Found ;(((")
            sys.exit()
        if "http://" or "https://" not in target:
            target = "https://" + target
        info = builtwith.parse(target)
        print("")
        count = 1
        for keys,values in info.items():
            print(Fore.GREEN + f" [{str(count)}] " + Fore.YELLOW + keys + "   :   " +Fore.CYAN + str(values))
            count += 1
        input(Fore.YELLOW + "\n\n[!] ~ Press Enter The Back Meno ")
        #codeing for back the meno
