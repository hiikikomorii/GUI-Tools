try:
    import platform
    import psutil
    import pygetwindow as gw
    import os
    from datetime import date, datetime
    from colorama import Fore, init, Style
    import customtkinter as ctk
except ModuleNotFoundError:
    import sys
    import subprocess
    boot_path = "bootstrapper/bootstrapper.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

init(autoreset=True)


class Util:
    def __init__(self, label_mon_m, label_mem_m, label_cpu_m, label_info_monitor_m):
        self.label_mon_m = label_mon_m
        self.label_mem_m = label_mem_m
        self.label_cpu_m = label_cpu_m
        self.label_info_monitor_m = label_info_monitor_m

    def monitoring_start(self, label_mon_m, label_mem_m, label_cpu_m, label_info_monitor_m):
        win = gw.getActiveWindow()

        self.label_info_monitor_m.configure(text=f"Name: {platform.node()}\n\n"
                                            f"OS: {platform.platform()}\n\n"
                                            f"Machine: {platform.machine()}\n\n"
                                            f"processor:  {platform.processor()}\n\n"
                                            f"CPU count:  {psutil.cpu_count()}\n\n"
                                            f"CPU usage: {psutil.cpu_percent(interval=1)}\n\n"
                                            f"Py version:  {platform.python_version()}\n\n"
                                            f"Py build:  {platform.python_build()}\n\n"
                                            f"Py compiler:  {platform.python_compiler()}\n\n"
                                            f"Script PID: {os.getpid()}\n\n"
                                            f"Window: {win.width}x{win.height}\n\n"
                                            f"Path: {__file__}")
        label_info_monitor_m.place(x=10, y=10)
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} MONITORING: {Fore.MAGENTA}Monitoring{Fore.RESET} | {Fore.LIGHTGREEN_EX}was enabled")
        while True:
            try:
                t = datetime.now().strftime("%H:%M:%S")
                self.label_mon_m.configure(text=f"\rTime: {t}")
                print(end="", flush=True)
                label_mon_m.place(x=550, y=10)

                mem = psutil.virtual_memory()
                self.label_mem_m.configure(text=f"\rИспользовано {mem.percent}% RAM")
                label_mem_m.place(x=550, y=50)

                cpu = psutil.cpu_percent(interval=1)
                self.label_cpu_m.configure(text=f"\rИспользовано {cpu}% CPU")
                label_cpu_m.place(x=550, y=90)


            except RuntimeError:
                return
