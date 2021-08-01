def dnslookup():
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
    target =  input(Fore.RED+" ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Dns-Lookup"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None or len(target) <= 1:
        time.sleep(1)
        print(Fore.RED + "\n[!] Error Your Target Is Not Found")
        #time.sleep(1)
        #sys.exit()
    if "http://" or "https://" not in target:
        target = "https://" + target
    url_me = "https://api.hackertarget.com/dnslookup/?q="
    R = requests.get(url_me+target).text
    print(Fore.GREEN + f"\n{R}")
    time.sleep(1)
    input(Fore.YELLOW + "\n\n[!] ~ Press Enter The Back Meno ")
    #codeing for back the meno
  except:
    pass
