def bootstrapper():
    import subprocess
    import sys
    boot_path = "../bootstrapper.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

try:
    from colorama import init, Fore, Style
except ModuleNotFoundError:
    bootstrapper()

init(autoreset=True)


def ping_faker_all():
    try:
        from faker import Faker
        try:
            fake_eng = Faker()
            fake_ru = Faker('Ru_ru')
            fake_es = Faker('es_ES')
            fake_jp = Faker('ja_JP')

            print(f"""{Style.BRIGHT}
Module: {Fore.MAGENTA}faker{Fore.RESET} | {Fore.LIGHTGREEN_EX}True{Fore.RESET}\n
Faker {Fore.MAGENTA}ENG{Fore.RESET} | example: city: '{Fore.MAGENTA}{fake_eng.city()}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True{Fore.RESET}
Faker {Fore.MAGENTA}RU{Fore.RESET} | example: city: '{Fore.MAGENTA}{fake_ru.city()}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True{Fore.RESET}
Faker {Fore.MAGENTA}ES{Fore.RESET} | example: city: '{Fore.MAGENTA}{fake_es.city()}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True{Fore.RESET}
Faker {Fore.MAGENTA}JP{Fore.RESET} | example: city: '{Fore.MAGENTA}{fake_jp.city()}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True
            """)
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{e}")
    except ModuleNotFoundError:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Module 'Faker' not defined")
        print(f"{Style.BRIGHT}Do you want download 'Faker'?")
        while True:
            bt = input("y/n: ").strip().lower()
            if bt == "y":
                bootstrapper()
            elif bt == "n":
                break
            else:
                pass


def ping_qrcode():
    try:
        import qrcode
        import os
        try:
            img = qrcode.make("https://github.com/hiikikomorii")
            img.save("qrcode.png")
            print(f"{Style.BRIGHT}Module: '{Fore.MAGENTA}qrcode{Fore.RESET}' | example: '{Fore.MAGENTA}qrcode.png{Fore.RESET}' ({Fore.LIGHTRED_EX}removed{Fore.RESET}) | {Fore.LIGHTGREEN_EX}True")
            os.remove("qrcode.png")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{e}")

    except ModuleNotFoundError:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Module 'qrcode' not defined")
        print(f"{Style.BRIGHT}Do you want download 'qrcode'?")
        while True:
            bt = input("y/n: ").strip().lower()
            if bt == "y":
                bootstrapper()
            elif bt == "n":
                break
            else:
                pass

def ping_ctypes():
    import ctypes
    import threading
    try:
        threading.Thread(target=lambda: ctypes.windll.user32.MessageBoxW(0, "True", "Test", 0x40), daemon=True).start()
        print(f"{Style.BRIGHT}Module: '{Fore.MAGENTA}ctypes{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True")
        print(f"{Style.BRIGHT}Module: '{Fore.MAGENTA}threading{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True")
        print(f"{Style.BRIGHT}example: {Fore.MAGENTA}Notification{Fore.RESET} | {Fore.LIGHTGREEN_EX}True")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}{e}")

def ping_monitoring():
    try:
        import platform
        import psutil
        import pygetwindow as gw
        try:
            win = gw.getActiveWindow()
            print(f"""{Style.BRIGHT}
Module '{Fore.MAGENTA}platform{Fore.RESET}' | example: Node: '{Fore.MAGENTA}{platform.node()}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True{Fore.RESET}
Module '{Fore.MAGENTA}psutil{Fore.RESET}' | example: CPU count: '{Fore.MAGENTA}{psutil.cpu_count()}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True{Fore.RESET}
Module '{Fore.MAGENTA}pygetwindow{Fore.RESET}' | example: Window:'{Fore.MAGENTA}{win.width}x{win.height}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}True

            """)
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{e}")

    except ModuleNotFoundError as mod:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Module '{mod.name}' not defined")
        print(f"{Style.BRIGHT}Do you want download '{mod.name}'?")
        while True:
            bt = input("y/n: ").strip().lower()
            if bt == "y":
                bootstrapper()
            elif bt == "n":
                break
            else:
                pass

def main():
    while True:
        user = input("> ")
        if user == "1":
            ping_faker_all()
        elif user == "2":
            ping_qrcode()
        elif user == "3":
            ping_ctypes()
        elif user == "4":
            ping_monitoring()
if __name__ == '__main__':
    main()