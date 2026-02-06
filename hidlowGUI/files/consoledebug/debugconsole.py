import os
import time
import sys
import subprocess
def bootstrapper():
    boot_path = "../bootstrapper/bootstrapper.py"
    subprocess.Popen(["cmd", "/c", sys.executable, str(boot_path)], creationflags=subprocess.CREATE_NEW_CONSOLE)
    sys.exit()

try:
    from colorama import init, Fore, Style
    import requests
except ModuleNotFoundError as e:
    bootstrapper()

init(autoreset=False)


class Prepare_check:
    def __init__(self):
        self._ping_api = None
        self._mod = None

    @property
    def api(self):
        if self._ping_api is None:

            import pingapi_func
            self._ping_api = pingapi_func
        return self._ping_api

    @property
    def mod(self):
        if self._mod is None:
            import ping_utils
            self._mod = ping_utils
        return self._mod

    def prepare_ping_number(self):
        try:
            import random
            from phonenumbers import carrier, geocoder, timezone, parse, is_valid_number
            import urllib.request
            import re
        except ModuleNotFoundError:
            bootstrapper()

        print(Fore.LIGHTWHITE_EX + "\rwait..", end="", flush=True)
        phone = re.sub(r"\D", "", "+79268471359")

        if self.api.check_internet():
            print(self.api.try_ping_number(phone))
        else:
            print(f"{Fore.RED}Отсутствует интернет-соединение!")

    def prepare_ip(self):
        self.api.try_ping_ip()

    def prepare_ll(self):
        self.api.try_ping_ll()

    def prepare_btc(self):
        self.api.try_ping_btc()

    def prepare_ton(self):
        self.api.try_ping_ton()

    def prepare_ping_faker(self):
        self.mod.ping_faker_all()

    def prepare_ping_qrcode(self):
        self.mod.ping_qrcode()

    def prepare_ping_ctypes(self):
        self.mod.ping_ctypes()

    def prepare_ping_monitor(self):
        self.mod.ping_monitoring()


class Info:
    def __init__(self):
        import socket
        from datetime import date, datetime
        self._win = None
        self._psutil = None
        self.ipv4 = requests.get("https://api.ipify.org").text
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.time1 = datetime.now().strftime("%H:%M:%S")
        self.data1 = date.today()

        self.help_text = f"""{Style.BRIGHT}
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

        {Fore.LIGHTBLUE_EX}-/> ping utils </-{Fore.RESET}{Fore.LIGHTWHITE_EX}
    ping number - проверяет Number API на работоспособность
    ping ip - проверяет IP API на работоспособность
    ping geo - проверяет  Lat/Lon API на работоспособность
    ping btc - проверяет BTC API на работоспособность
    ping ton - проверяет TON API на работоспособность
    ping faker - проверяет модуль Faker и его работоспособность
    ping qrcode - проверяет модуль qrcode и его работоспособность
    ping ctypes - проверяет работоспособность уведомлений в ctypes
    ping monitoring - проверяет модуль pssutil, platform и т.д, и их работоспособность"""

    def load_conf_info(self):
        if self._win is None:
            try:
                import pygetwindow as gw
                self._win = gw.getActiveWindow()
            except ModuleNotFoundError:
                bootstrapper()

        if self._psutil is None:
            try:
                import psutil
                self._psutil = psutil
            except ModuleNotFoundError:
                bootstrapper()

    def conf_info(self):
        self.load_conf_info()
        import platform
        try:
            print(f"{Fore.WHITE}Name:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.node()}")
            print(f"{Fore.WHITE}OS:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.platform()}")
            print(f"{Fore.WHITE}Machine:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.machine()}")
            print(f"{Fore.WHITE}processor:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.processor()}")
            print(f"{Fore.WHITE}CPU count:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {self._psutil.cpu_count()}")
            print(f"{Fore.WHITE}Memory:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {self._psutil.virtual_memory()}")
            print(f"{Fore.WHITE}Script PID:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {os.getpid()}")
            if self._win:
                print(f"{Fore.WHITE}Window size:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {self._win.width}x{self._win.height}")
            else:
                print(f"{Fore.WHITE}Window size: {Fore.LIGHTRED_EX}{Style.BRIGHT}Active window is not definded")
            print(f"{Fore.WHITE}Sctipt dir:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {__file__}\n")

            print(f"{Fore.WHITE}Py Version:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.python_version()}")
            print(f"{Fore.WHITE}Py Build:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.python_build()}")
            print(f"{Fore.WHITE}Py Compiler:{Fore.LIGHTWHITE_EX}{Style.BRIGHT} {platform.python_compiler()}")
        except Exception as error_sysinfo:
            print(f"{Fore.RED}error info about system\n{error_sysinfo}")

    def check_ip(self):
        print(f"{Fore.WHITE}IPv4: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{self.ipv4}")
        print(f"{Fore.WHITE}Local IP: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{self.local_ip}")

    def date(self):
        print(f"{Fore.WHITE}date: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{self.data1}", end=" | ")
        print(f"{Fore.WHITE}time: {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{self.time1}")


class Main:
    def __init__(self):
        self.reboot_path = os.path.abspath(__file__)
        self._ORIGINAL_WHITE = Fore.WHITE
        self._ORIGINAL_LIGHT = Fore.LIGHTWHITE_EX
        self.base_color = None
        self.light_color = None
        self.info = Info()
        self.check = Prepare_check()

        self.commands = {
            "clear": lambda: os.system("cls"),
            "exit": sys.exit,
            "info": self.info.conf_info,
            "myip": self.info.check_ip,
            "help": lambda: print(self.info.help_text),
            "time": self.info.date,
            "reboot": self.reboot,
            "fg blue": lambda: self.set_theme("blue"),
            "fg cyan": lambda: self.set_theme("cyan"),
            "fg red": lambda: self.set_theme("red"),
            "fg white": lambda: self.set_theme("nn"),
            "fg": self.fg_arg,
            "ping number": self.check.prepare_ping_number,
            "ping ip": self.check.prepare_ip,
            "ping geo": self.check.prepare_ll,
            "ping btc": self.check.prepare_btc,
            "ping ton": self.check.prepare_ton,
            "ping faker": self.check.prepare_ping_faker,
            "ping qrcode": self.check.prepare_ping_qrcode,
            "ping ctypes":self.check.prepare_ping_ctypes,
            "ping monitoring": self.check.prepare_ping_monitor,
            "ping": self.ping_arg
        }
    def run(self):
        while True:
            cmd = input(Fore.WHITE + "> ").strip().lower()
            action = self.commands.get(cmd)
            if not cmd:
                continue
            if cmd in self.commands:
                action()
            else:
                print(f"{Style.BRIGHT}{Fore.RED}неизвестная команда: {cmd}. Введите 'help' для списка команд.")

    def reboot(self):
        try:
            subprocess.Popen(
                ["cmd", "/c", sys.executable, str(self.reboot_path)],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            sys.exit()
        except Exception as error_reboot:
            print(f"{Fore.RED} Reboot error.\n{error_reboot}")

    @staticmethod
    def ping_arg():
        print(f"{Fore.LIGHTWHITE_EX}api: number | ip | geo | btc | ton")
        print(f"{Fore.LIGHTWHITE_EX}utils: faker | qrcode | ctypes | monitoring")

    @staticmethod
    def fg_arg():
        print(f"{Fore.LIGHTWHITE_EX}fg white | fg blue | fg cyan | fg red")

    def set_theme(self, color_name):
        if color_name.lower() == "white":
            self.base_color = self._ORIGINAL_WHITE
            self.light_color = self._ORIGINAL_LIGHT
        else:
            self.base_color = getattr(Fore, color_name.upper(), self._ORIGINAL_WHITE)
            self.light_color = getattr(Fore, f"LIGHT{color_name.upper()}_EX", self._ORIGINAL_LIGHT)

        Fore.WHITE = self.base_color
        Fore.LIGHTWHITE_EX = self.light_color

if __name__ == "__main__":
    app = Main()
    app.run()