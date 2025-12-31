import os
import time
import sys

def nomodule_boottraper():

    import subprocess
    boot_path = "../../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

try:
    from colorama import init, Fore, Style
    import requests
except ModuleNotFoundError as e:
    import ctypes
    if e.name == "pingapi_func":
        ctypes.windll.user32.MessageBoxW(0, f"Сборка повреждена\nПапка {e.name} не найдена\nПроверьте совместимость сборки", "debug-console", 0x10)
        sys.exit()
    nomodule_boottraper()


init(autoreset=False)
_orig_white = Fore.WHITE
_orig_white_ex = Fore.LIGHTWHITE_EX


def help_cmd():
    print(f"""{Style.BRIGHT}
    {Fore.LIGHTBLUE_EX}-/> system & info </-{Fore.RESET}{Fore.LIGHTWHITE_EX}
help - список комманд
clear - очищает консоль
reboot - перезагрузка скрипта
exit - выход
info - выводит информацию о системе
myip - выводит ipv4 и локальный ip
time - актуальная дата и время

    {Fore.LIGHTBLUE_EX}-/> console color </-{Fore.RESET}{Fore.LIGHTWHITE_EX}
fg blue - меняет цвет консоли на синий
fg cyan - меняет цвет консоли на голубой
fg red - меняет цвет консоли на красный
fg white - меняет цвет консоли на белый
    
    {Fore.LIGHTBLUE_EX}-/> ping utils 
    
    </-{Fore.RESET}{Fore.LIGHTWHITE_EX}
ping number - проверяет Number API на работоспособность
ping ip - проверяет IP API на работоспособность
ping latlon - проверяет  Lat/Lon API на работоспособность
ping btc - проверяет BTC API на работоспособность
ping ton - проверяет TON API на работоспособность
ping faker - проверяет модуль Faker и его работоспособность
ping qrcode - проверяет модуль qrcode и его работоспособность
ping ctypes - проверяет работоспособность уведомлений в ctypes
ping monitoring - проверяет модуль pssutil, platform и т.д, и их работоспособность
""")


def clear_cmd():
    os.system("cls")


def exit_cmd():
    print(Fore.RED + "Выход...")
    sys.exit()

def info_cmd():
    try:
        import psutil, platform
    except ModuleNotFoundError:
        nomodule_boottraper()
    sys1 = platform.node()
    sys2 = platform.platform()
    sys3 = platform.machine()
    sys4 = platform.processor()
    sys5 = psutil.cpu_count()
    sys6 = psutil.virtual_memory()
    syspy1 = platform.python_version()
    syspy2 = platform.python_build()
    syspy3 = platform.python_compiler()
    os1 = os.getpid()
    try:
        print(f"{Fore.WHITE}Name:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {sys1}")
        print(f"{Fore.WHITE}OS:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {sys2}")
        print(f"{Fore.WHITE}Machine:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {sys3}")
        print(f"{Fore.WHITE}processor:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {sys4}")
        print(f"{Fore.WHITE}CPU count:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {sys5}")
        print(f"{Fore.WHITE}Memory:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {sys6}")
        print(f"{Fore.WHITE}Script PID:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {os1}")

        print(f"{Fore.WHITE}Py Version:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {syspy1}")
        print(f"{Fore.WHITE}Py Build:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {syspy2}")
        print(f"{Fore.WHITE}Py Compiler:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {syspy3}")


    except Exception as error_sysinfo:
        print(f"{Fore.RED}error info about system\n{error_sysinfo}")


def reboot_cmd():
    import subprocess
    try:
        script_path = os.path.abspath(__file__)
        subprocess.Popen(
            ["cmd", "/c", sys.executable, str(script_path)],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        time.sleep(2)
        sys.exit()
    except Exception as error_reboot:
        print(f"{Fore.RED} Reboot error.\n{error_reboot}")

def ipconfig_cmd():
    import socket
    ipv4 = requests.get("https://api.ipify.org").text
    local_ip = socket.gethostbyname(socket.gethostname())

    print(f"{Fore.WHITE}IPv4: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{ipv4}")
    print(f"{Fore.WHITE}Local IP: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{local_ip}")


def date_cmd():
    from datetime import date, datetime
    time1 = datetime.now().strftime("%H:%M:%S")
    data1 = date.today()

    print(f"{Fore.WHITE}date: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{data1}", end=" | ")
    print(f"{Fore.WHITE}time: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{time1}")


def onlyfgarg():
    print(Fore.LIGHTWHITE_EX + "fg red, blue, cyan, white")
def fgred_cmd():
    Fore.WHITE = Fore.RED
    Fore.LIGHTWHITE_EX = Fore.LIGHTRED_EX
def fgwhite_cmd():
    Fore.WHITE = _orig_white
    Fore.LIGHTWHITE_EX = _orig_white_ex
def fgblue_cmd():
    Fore.WHITE = Fore.BLUE
    Fore.LIGHTWHITE_EX = Fore.LIGHTBLUE_EX
def fgcyan_cmd():
    Fore.WHITE = Fore.CYAN
    Fore.LIGHTWHITE_EX = Fore.LIGHTCYAN_EX


def prepare_ping_number():
    try:
        from pingapi_func import try_ping_number, check_internet
        import random
        from phonenumbers import carrier, geocoder, timezone, parse, is_valid_number
        import urllib.request
        import re
    except ModuleNotFoundError:
        nomodule_boottraper()

    print(Fore.LIGHTWHITE_EX + "\rwait..", end="", flush=True)
    user_iput = "+79268471359"
    phone = re.sub(r"\D", "", user_iput)

    if check_internet():
        a = try_ping_number(phone)
        print(a)
    else:
        print(f"{Fore.RED}Отсутствует интернет-соединение!")

def prepare_ip():
    from pingapi_func import try_ping_ip
    try_ping_ip()

def prepare_ll():
    from pingapi_func import try_ping_ll
    try_ping_ll()

def prepare_btc():
    from pingapi_func import try_ping_btc
def prepare_ton():
    from pingapi_func import try_ping_ton

def prepare_onlypingarg():
    from pingapi_func import onlypingarg
    onlypingarg()

def prepare_ping_faker():
    from ping_utils import ping_faker_all
    ping_faker_all()

def prepare_ping_qrcode():
    from ping_utils import ping_qrcode
    ping_qrcode()

def prepare_ping_ctypes():
    from ping_utils import ping_ctypes
    ping_ctypes()

def prepare_ping_monitor():
    from ping_utils import ping_monitoring
    ping_monitoring()

def main():

    commands = {
        "clear": clear_cmd,
        "exit": exit_cmd,
        "info": info_cmd,
        "myip": ipconfig_cmd,
        "help": help_cmd,
        "time": date_cmd,
        "reboot": reboot_cmd,
        "fg blue": fgblue_cmd,
        "fg cyan": fgcyan_cmd,
        "fg red": fgred_cmd,
        "fg white": fgwhite_cmd,
        "fg": onlyfgarg,
        "ping number": prepare_ping_number,
        "ping ip": prepare_ip,
        "ping latlon": prepare_ll,
        "ping btc": prepare_btc,
        "ping ton": prepare_ton,
        "ping faker": prepare_ping_faker,
        "ping qrcode": prepare_ping_qrcode,
        "ping ctypes": prepare_ping_ctypes,
        "ping monitoring": prepare_ping_monitor,
        "ping": prepare_onlypingarg
    }


    while True:
        cmd = input(Fore.WHITE + "> ").strip().lower()
        if not cmd:
            continue
        if cmd in commands:
            commands[cmd]()
        else:
            print(f"{Style.BRIGHT}{Fore.RED}неизвестная команда: {cmd}. Введите 'help' для списка команд.")

if __name__ == '__main__':
    main()