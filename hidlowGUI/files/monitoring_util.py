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
    win = gw.getActiveWindow()

    label_info_monitor_m.configure(text=f"Name: {platform.node()}\n\n"
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
    label_info_monitor_m.pack(padx=5)
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
def example_test():
    import customtkinter as ctk
    import threading as thr
    root = ctk.CTk()

    monitor_frame = ctk.CTkFrame(root, fg_color="#242424")
    monitor_frame.pack(pady=20, anchor="n")
    monitor_frame_stat = ctk.CTkFrame(root, fg_color="#242424")
    monitor_frame_stat.pack(pady=10, anchor="sw", side="left")
    label_mon = ctk.CTkLabel(monitor_frame, font=("Arial", 30))
    label_mem = ctk.CTkLabel(monitor_frame, font=("Arial", 30))
    label_cpu = ctk.CTkLabel(monitor_frame, font=("Arial", 30))
    label_info_monitor = ctk.CTkLabel(monitor_frame_stat, font=("Arial", 20))

    thr.Thread(target=lambda: monitoring_start(label_mon, label_mem, label_cpu, label_info_monitor),daemon=True).start()
    root.mainloop()
if __name__ == '__main__':
 example_test()