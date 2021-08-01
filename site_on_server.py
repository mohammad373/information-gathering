def site_on_server():
  try:
    import os
    import time
    import sys
    import json
    import requests
    from baner import baner
    from colorama import Fore

    os.system("clear")
    baner()
    time.sleep(1)
    target =  input(Fore.RED+" ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Site-On-Server"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    #if "https://" or "http://" not in target:
    #    target = "https://" + target
    data_me = {"remoteAddress" : target}
    url = requests.post("https://domains.yougetsignal.com/domains.php",data_me)
    info = json.loads(url.content)
    print("")
    count = 1
    for i in info["domainArray"]:
      if "https://" or "http://" not in i[0]:
        i = "https://" + i[0]
        data_me = Fore.LIGHTBLACK_EX + f"[{count}] ~ "   + Fore.CYAN + str(i)
      else:
        data_me = Fore.LIGHTBLACK_EX + f"[{count}] ~ "   + Fore.CYAN + str(i[0])
      print(data_me)
      count += 1
    input(Fore.YELLOW + "\n\n[!] ~ Press Enter The Back Meno ")
    #codeing for back the meno
  except:
    pass
