try:
    import platform
    import psutil
    import pygetwindow as gw
    import os
    from datetime import date, datetime
    from colorama import Fore, init, Style
except ModuleNotFoundError:
    import sys
    import subprocess
    boot_path = "../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

init(autoreset=True)
def monitoring_start(label_mon_m, label_mem_m, label_cpu_m, label_info_monitor_m):
    sys1 = platform.node()
    sys2 = platform.platform()
    sys3 = platform.machine()
    sys4 = platform.processor()
    sys5 = psutil.cpu_count()
    sys6 = psutil.cpu_percent(interval=1)
    os1 = os.getpid()
    win = gw.getActiveWindow()
    path_mon = __file__

    syspy1 = platform.python_version()
    syspy2 = platform.python_build()
    syspy3 = platform.python_compiler()

    label_info_monitor_m.configure(text=f"Name: {sys1}\n\n"
                                      f"OS: {sys2}\n\n"
                                      f"Machine: {sys3}\n\n"
                                      f"processor:  {sys4}\n\n"
                                      f"CPU count:  {sys5}\n\n"
                                      f"CPU usage: {sys6}\n\n"
                                      f"Py version:  {syspy1}\n\n"
                                      f"Py build:  {syspy2}\n\n"
                                      f"Py compiler:  {syspy3}\n\n"
                                      f"Script PID: {os1}\n\n"
                                      f"Window: {win.width}x{win.height}\n\n"
                                      f"Path: {path_mon}")
    label_info_monitor_m.pack(pady=5)
    print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} MONITORING: {Fore.MAGENTA}Monitoring{Fore.RESET} | {Fore.LIGHTGREEN_EX}was enabled")
    while True:
        try:
            t = datetime.now().strftime("%H:%M:%S")
            label_mon_m.configure(text=f"\r{t}")
            print(end="", flush=True)
            label_mon_m.pack()

            mem = psutil.virtual_memory()
            label_mem_m.configure(text=f"\rИспользовано {mem.percent}% RAM")
            label_mem_m.pack()

            cpu = psutil.cpu_percent(interval=1)
            label_cpu_m.configure(text=f"\rИспользовано {cpu}% CPU")
            label_cpu_m.pack()


        except RuntimeError:
            return