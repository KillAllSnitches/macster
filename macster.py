import os, time
from colorama import init, Style, Fore
import ctypes
import requests
import json
cyan = Fore.LIGHTCYAN_EX
orange = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL
bright = Style.BRIGHT
off = 'adb shell "su -c \'busybox ifconfig wlan0 down;\'"'
on = 'adb shell "su -c \'busybox ifconfig wlan0 up;\'"'
one = 'adb shell "su -c \'busybox ifconfig wlan0 hw ether '
two ='\'\"'
cmd = os.system
init()
def initialize():
    cmd('echo on')
    logo()
    print(green, 'Checking if ADB Daemon is Running...')
    time.sleep(0.3)
    cmd('adb start-server')
    logo()
    print(green, 'ADB Daemon Running!')
    time.sleep(0.5)
    main()
def clear():
    if os.name == 'nt':
        cmd('cls')
    else:
        cmd('clear')
def logo():
    clear()
    cmd('mode con: cols=80 lines=40')
    ctypes.windll.kernel32.SetConsoleTitleW("MACSTER | vx#1234")
    print(bright, cyan + """         
            ███╗   ███╗ █████╗  ██████╗███████╗████████╗███████╗██████╗ 
            ████╗ ████║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
            ██╔████╔██║███████║██║     ███████╗   ██║   █████╗  ██████╔╝
            ██║╚██╔╝██║██╔══██║██║     ╚════██║   ██║   ██╔══╝  ██╔══██╗
            ██║ ╚═╝ ██║██║  ██║╚██████╗███████║   ██║   ███████╗██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                            github.com/vx-dev/macster
                                                            """ + reset)
def error():
    logo()
    print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
    time.sleep(5)
    main()
def main():
    logo()
    print("""
        [""" + cyan + """1""" + reset + """] Mac Spoofer
        [""" + cyan + """2""" + reset + """] Mac Checker
        [""" + cyan + """3""" + reset + """] Mac Lookup
        [""" + cyan + """4""" + reset + """] Exit
        
        """)
    mode = input('Mode: ')
    if mode == '1':
        spoofmenu()
    elif mode == '2':
        check()
    elif mode == '3':
        lookup()
    elif mode == '4':
        logo()
        print(red, 'Stopping ADB Daemon...')
        cmd('adb kill-server')
        time.sleep(0.3)
        logo()
        print(red, 'ADB Daemon Stopped!')
        time.sleep(0.5)
        cmd('cls')
        exit
    else:
        logo()
        print("Error!")
        time.sleep(0.6)
        main()
def check():
    try:
        logo()
        cmd('adb shell "su -c \'busybox iplink show wlan0\'"')
        print("""
        the first address is your phone\'s current mac address""")
        time.sleep(5)
        main()
    except:
        error()
def lookup():
    logo()
    print('Enter MAC Address')
    mac = input('')
    url = "https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/"

    querystring = {"query":"18:93:d7:3e:1d:ad"}

    headers = {
    'x-rapidapi-key': "871a5edf01msh02dee63a8bb4f38p108c2ajsn65e747eb0d08",
    'x-rapidapi-host': "mac-address-lookup1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    r = response.json()
    if response.text == '{\"message\":\"You have exceeded the rate limit per second for your plan, BASIC, by the API provider\"}':
        logo()
        print(orange, "You're being rate limited!", reset)
        time.sleep(1.3)
        lookup()
    elif response.text == '{"message":"You have exceeded the DAILY quota for Requests on your current plan, BASIC. Upgrade your plan at https:\/\/rapidapi.com\/softrix-technologies-dnschecker\/api\/mac-address-lookup1"}':
        logo()
        print(red, "Current api key is locked for 24h, try again with a different key & ip address!", reset)
        lookup1()
    else:
        logo()
        print("MAC Address: "+mac)
        for i in 'name', 'address':
            print(f"{i.capitalize()}:{r['result'][0][i]}")
        c = input('Press Any Key to Continue')
        if c == 'a':
            main()
        else:
            main()
def lookup1():
    logo()
    print('Enter MAC Address')
    mac = input('')
    url = "https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/"

    querystring = {"query":"18:93:d7:3e:1d:ad"}

    headers = {
    'x-rapidapi-key': "c25faacaaamsh53b22411edd67e9p199c6bjsn387094dd33c1",
    'x-rapidapi-host': "mac-address-lookup1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    r = response.json()
    if response.text == '{\"message\":\"You have exceeded the rate limit per second for your plan, BASIC, by the API provider\"}':
        logo()
        print(orange, "You're being rate limited!", reset)
        time.sleep(1.3)
        lookup()
    elif response.text == '{"message":"You have exceeded the DAILY quota for Requests on your current plan, BASIC. Upgrade your plan at https:\/\/rapidapi.com\/softrix-technologies-dnschecker\/api\/mac-address-lookup1"}':
        logo()
        print(red, "All keys are locked, try again later.", reset)
        time.sleep(3)
        main()
    else:
        logo()
        print("MAC Address: "+mac)
        for i in 'name', 'address':
            print(f"{i.capitalize()}:{r['result'][0][i]}")
def spoofmenu():
    logo()
    print("""
        [""" + cyan + """1""" + reset + """] Custom Mac Address
        [""" + cyan + """2""" + reset + """] Preset Mac Address
        [""" + cyan + """3""" + reset + """] Automatic (Spoofs Your Mac Address Every 15 Minutes)
        [""" + cyan + """4""" + reset + """] Go Back
        """)
    mode = input('Mode: ')
    if mode == '1':
        customspoof()
    elif mode == '2':
        presetspoof()
    elif mode == '3':
        autospoof()
    elif mode == '4':
        main()
def customspoof():
    try:
        logo()
        mac = input('Mac Address: ')
        cmd(on)
        cmd(one+mac+two)
        cmd(off)
        logo()
        print("Spoofing Finished!")
        print("your device might not display the proper mac address if you're unsure run the mac address checker")
        time.sleep(3)
        main()
    except:
        print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
        time.sleep(5)
        main()
def presetspoof():
    logo()
    print("""
        [""" + cyan + """1""" + reset + """] 64:b5:c6:23:d4:fa
        [""" + cyan + """2""" + reset + """] 00:50:c2:8c:dd:38
        [""" + cyan + """3""" + reset + """] b0:fd:0b:4c:30:bc
        [""" + cyan + """4""" + reset + """] 10:0d:7f:ed:1c:78
        [""" + cyan + """5""" + reset + """] f4:62:d0:7e:05:72
    
        """)
    choice = input('')
    if choice == '1':
        try:
            mac = "64:b5:c6:23:d4:fa"
            cmd(off)
            cmd(one+mac+two)
            cmd(on)
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except():
            error()
    elif choice == '2':
        try:
            mac = "00:50:c2:8c:dd:38"
            cmd(off)
            cmd(one+mac+two)
            cmd(on)
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            error()
    elif choice == '3':
        try:
            mac = "f4:62:d0:7e:05:72"
            cmd(on)
            cmd(one+mac+two)
            cmd(off)
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            error()
    elif choice == '4':
        try:
            mac = "70:b3:d5:aa:e6:95"
            cmd(on)
            cmd(one+mac+two)
            cmd(off)
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            error()
    elif choice == '5':
        try:
            mac = "00:19:f0:dc:70:d0"
            cmd(on)
            cmd(one+mac+two)
            cmd(off)
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            error()
def autospoof():
    mac1 = "00:50:c2:76:96:b9"
    mac2 = "f0:de:f1:89:6e:25"
    mac3 = "98:ae:71:6f:1f:a9"
    mac4 = "d8:86:0b:2a:0d:25"
    mac5 = "00:50:8b:71:bd:57"
    mac6 = "70:b3:d5:ad:2f:6d"
    mac7 = "00:01:6f:c1:8c:9d"
    mac8 = "00:0c:7f:f5:74:c7"
    mac9 = "00:e0:88:f5:d9:00"
    mac10 = "44:7e:95:db:be:89"
    mac11 = "00:17:e5:fb:42:f3"
    mac12 = "28:31:66:ad:d9:2b"
    mac13 = "00:90:93:5d:c6:1d"
    mac14 = "ac:a4:6e:69:2c:c6"
    mac15 = "00:19:d6:a7:a1:9e"
    spoofed = "Spoofed MAC Address!"
    loopstart = "~ Start of Loop ~"
    loopend = "~ End of Loop ~"
    try:
        logo()
        print(orange, loopstart)
        cmd(off)
        cmd(one+mac1+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac2+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac3+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac4+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac5+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac6+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac7+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac8+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac9+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac10+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac11+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac12+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac13+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac14+two)
        cmd(on)
        print(green, spoofed)
        time.sleep(900)
        cmd(off)
        cmd(one+mac15+two)
        cmd(on)
        print(green, spoofed)
        print(orange, loopend)
        time.sleep(900)
        autospoof()
    except:
        cmd(on)
        error()
initialize()
