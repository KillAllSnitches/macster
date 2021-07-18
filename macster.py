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
    os.system('mode con: cols=80 lines=40')
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

def spoofmenu():
    logo()
    print("""
        [""" + Fore.LIGHTCYAN_EX + """1""" + Style.RESET_ALL + """] Custom Mac Address
        [""" + Fore.LIGHTCYAN_EX + """2""" + Style.RESET_ALL + """] Preset Mac Address

        """)
    mode = input('Mode: ')
    if mode == '1':
        customspoof()
    elif mode == '2':
        presetspoof()
def customspoof():
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
def presetspoof():
    logo()
    print("""
        [""" + Fore.LIGHTCYAN_EX + """1""" + Style.RESET_ALL + """] 64:b5:c6:23:d4:fa
        [""" + Fore.LIGHTCYAN_EX + """2""" + Style.RESET_ALL + """] 00:50:c2:8c:dd:38
        [""" + Fore.LIGHTCYAN_EX + """3""" + Style.RESET_ALL + """] b0:fd:0b:4c:30:bc
        [""" + Fore.LIGHTCYAN_EX + """4""" + Style.RESET_ALL + """] 10:0d:7f:ed:1c:78
        [""" + Fore.LIGHTCYAN_EX + """5""" + Style.RESET_ALL + """] f4:62:d0:7e:05:72
    
        """)
    choice = input('')
    if choice == '1':
        try:
            mac = "64:b5:c6:23:d4:fa"
            os.system('adb shell "su -c \'busybox ifconfig wlan0 down;\'"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 hw ether '+mac+'\'\"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 up;\'"')
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
            time.sleep(5)
            main()
    elif choice == '2':
        try:
            mac = "00:50:c2:8c:dd:38"
            os.system('adb shell "su -c \'busybox ifconfig wlan0 down;\'"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 hw ether '+mac+'\'\"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 up;\'"')
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
            time.sleep(5)
            main()
    elif choice == '3':
        try:
            mac = "f4:62:d0:7e:05:72"
            os.system('adb shell "su -c \'busybox ifconfig wlan0 down;\'"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 hw ether '+mac+'\'\"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 up;\'"')
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
            time.sleep(5)
            main()
    elif choice == '4':
        try:
            mac = "70:b3:d5:aa:e6:95"
            os.system('adb shell "su -c \'busybox ifconfig wlan0 down;\'"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 hw ether '+mac+'\'\"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 up;\'"')
            logo()
            print("Spoofing Finished!")
            print("your device might not display the proper mac address if you're unsure run the mac address checker")
            time.sleep(3)
            main()
        except:
            print("An error has occured, please ensure that you have ADB installed on your computer & BusyBox installed on your android device")
            time.sleep(5)
            main()
    elif choice == '5':
        try:
            mac = "00:19:f0:dc:70:d0"
            os.system('adb shell "su -c \'busybox ifconfig wlan0 down;\'"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 hw ether '+mac+'\'\"')
            os.system('adb shell "su -c \'busybox ifconfig wlan0 up;\'"')
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
