import os, time
def initialize():
    clear()
    reqs()
from colorama import init, Style, Fore
import ctypes
init(convert=True)
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def logo():
    clear()
    os.system('mode con: cols=90 lines=50')
    ctypes.windll.kernel32.SetConsoleTitleW("MACSTER | vx#1234")
    print(Style.BRIGHT, Fore.LIGHTCYAN_EX + """         
            ███╗   ███╗ █████╗  ██████╗███████╗████████╗███████╗██████╗ 
            ████╗ ████║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
            ██╔████╔██║███████║██║     ███████╗   ██║   █████╗  ██████╔╝
            ██║╚██╔╝██║██╔══██║██║     ╚════██║   ██║   ██╔══╝  ██╔══██╗
            ██║ ╚═╝ ██║██║  ██║╚██████╗███████║   ██║   ███████╗██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                            github.com/vx-dev/macster
                                                            """ + Style.RESET_ALL)
def main():
    logo()
    print("""
        [""" + Fore.LIGHTCYAN_EX + """1""" + Style.RESET_ALL + """] Mac Spoofer
        [""" + Fore.LIGHTCYAN_EX + """2""" + Style.RESET_ALL + """] Mac Checker
        [""" + Fore.LIGHTCYAN_EX + """3""" + Style.RESET_ALL + """] Mac List
        
        """)
    mode = input('Mode: ')
    if mode == '1':
        spoof()
    elif mode == '2':
        check()
    elif mode == '3':
        list()
    else:
        logo()
        print("Error!")
        time.sleep(0.6)
        main()
def list():
    logo()
    print('List of Valid Mac Addresses:')
    print('')
    print("""70:b3:d5:32:ce:b4
64:b5:c6:23:d4:fa
00:50:c2:8c:dd:38
70:b3:d5:67:51:0a
00:50:24:27:5f:a8
00:07:c4:7d:e5:19
00:50:c2:f6:5e:77
00:20:93:13:98:ac
88:3d:24:4e:6a:38
00:10:21:b7:ef:2d
2c:8a:72:e8:2a:22
58:05:28:c2:e9:79
00:05:cd:4c:d8:96
8c:79:67:8f:a7:bc
a0:02:4a:a2:9b:bb
00:50:c2:c6:ab:7d
00:24:72:fe:73:26
00:16:f5:6e:ef:b9
20:16:d8:1e:21:6e
00:03:97:45:0c:9b
00:05:fa:76:8d:b3
48:43:dd:9b:f7:45
c8:8e:d1:1c:44:6e
1c:a0:ef:ab:eb:78

Returning to Main Menu in 5s...
""")
    time.sleep(5)
    main()
def check():
    try:
        logo()
        os.system('adb shell "su -c \'busybox iplink show wlan0\'"')
        print("""
        the first address is your phone\'s current mac address""")
        time.sleep(5)
        main()
    except:
        print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
        time.sleep(5)
        main()
def reqs():
    logo()
    print("""
    You Must Have the Following Installed to Use Macster
    - ADB (Android Platform Tools)
    - Rooted Android Device with BusyBox
    """)
    time.sleep(5)
    main()
def spoof():
    try:
        logo()
        mac = input('Mac Address: ')
        os.system('adb shell "su -c \'busybox ifconfig wlan0 down;\'"')
        os.system('adb shell "su -c \'busybox ifconfig wlan0 hw ether '+mac+'\'\"')
        os.system('adb shell "su -c \'busybox ifconfig wlan0 up;\'"')
        clear()
        logo()
        print("Spoofing Finished!")
        print("your device might not display the proper mac address if you're unsure run the mac address checker")
        time.sleep(3)
        main()
    except:
        print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
        time.sleep(5)
        main()
initialize()
