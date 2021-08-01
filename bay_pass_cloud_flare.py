def bay_pass_cloud_flare():
    import os
    import time
    import sys
    import socket
    from colorama import Fore
    from baner import baner

    os.system("clear")
    baner()
    time.sleep(1)
    target =  input(Fore.RED+" ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"PayPass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None or len(target) <= 1:
        time.sleep(1)
        print(Fore.RED + "\n[!] Error Your Input Is not Found ;(((")
        sys.exit()
    #if "http://" or "https://" not in target:
    #    target = "https://" + target
    my_sub = """
    www
    mail
    ftp
    webmail
    smtp
    pop
    ns1
    webdisk
    ns2
    cpanel
    whm
    autodiscover
    autoconfig
    m
    imap
    test
    ns
    blog
    pop3
    dev
    www2
    admin
    forum
    news
    vpn
    ns3
    mail2
    new
    mysql
    old
    lists
    support
    mobile
    mx
    static
    docs
    beta
    shop
    sql
    secure
    demo
    cp
    calendar
    wiki
    web
    media
    email
    images
    img
    www1
    intranet
    portal
    video
    sip
    dns2
    api
    cdn
    stats
    dns1
    ns4
    www3
    dns
    search
    staging
    server
    mx1
    chat
    wap
    my
    svn
    mail1
    sites
    proxy
    ads
    host
    crm
    cms
    backup
    mx2
    lyncdiscover
    info
    apps
    download
    remote
    db
    forums
    store
    relay
    files
    newsletter
    app
    live
    owa
    en
    start
    sms
    office
    exchange
    ipv4
    """.split()
    try:
      count = 1
      for i in my_sub:
        time.sleep(0.4)
        now_target = i + "." + target
        #print(now_target)
        ip_target = socket.gethostbyname(now_target)
        print(Fore.GREEN + f"[{str(count)}] {now_target}  | Ip : {ip_target}")
        count += 1
    except:
      pass
    input(Fore.YELLOW + "\n\n[!] ~ Press Enter The Back Meno ")
    #codeing for back the meno
