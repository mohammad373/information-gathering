def nmap():
  try:
    import os
    import time
    import sys
    from baner import baner
    from colorama import Fore
    import requests

    os.system("clear")
    baner()
    time.sleep(1)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.GREEN + "Enter Your Target  : " + Fore.YELLOW + " ")
    if target == "" or None or len(target) <= 1:
        time.sleep(1)
        print(Fore.RED + "\n[!] Error Your Target Is Not Found")
        #time.sleep(1)
        #sys.exit()
    if "http://" or "https://" not in target:
        target = "https://" + target
    url_me = "https://api.hackertarget.com/nmap/?q="
    R = requests.get(url_me+target).text
    print(Fore.GREEN + f"\n{R}")
    time.sleep(1)
    input(Fore.YELLOW + "\n\n[!] ~ Press Enter The Back Meno ")
    #codeing for back the meno
  except:
    pass
