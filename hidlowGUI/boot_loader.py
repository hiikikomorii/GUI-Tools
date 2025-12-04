import tkinter as tk
import subprocess
import sys
import threading
import os
import platform
import ctypes
from datetime import date, datetime
fullscreen = True
root = tk.Tk()
time1 = datetime.now().strftime("%H:%M:%S")
data1 = date.today()

try:
    import customtkinter
    import requests
    from PIL import Image, ImageTk
    import colorama
    import qrcode
    import psutil
    from phonenumbers import carrier, geocoder, timezone, parse, is_valid_number
    import phonenumbers
    from faker import Faker
    import pynput
    import test_module #test
    from flask import Flask, jsonify
    from files.consoledebug.pingapi_func import try_ping_number, send_request_ping, try_ping_ll, try_ping_btc, try_ping_ton, try_ping_ip, check_internet, onlypingarg


    hidlow_path = "HidlowToolsGUI.py"
    subprocess.Popen(
        ["cmd", "/k", sys.executable, str(hidlow_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    sys.exit()
except ModuleNotFoundError as e:
    if e.name == "files.consoledebug.pingapi_func":
        ctypes.windll.user32.MessageBoxW(0, f"Сборка повреждена\nпуть {e.name} не найден\nПроверьте совместимость сборки", "debug-console", 0x10)
        sys.exit()

    root.title("BOOT-LOADER-NOMODULE")
    root.attributes('-fullscreen', True)
    root.config(bg="blue")

    pybuild = platform.python_build()
    pycomp = platform.python_compiler()
    pyver = platform.python_version()


    def exit_bbt():
        root.destroy()
        sys.exit()


    text = ("""
Boottraped-menu\n
Скрипту не удалось запуститься из-за ошибки\n
Установите модули нажав кнопку 'Install'\n
Обновите pip нажав кнопку 'upgrade pip'\n
Нажав кнопку 'reboot' вы перезапускаете скрипт\n
если ошибок не возникнет - скрипт, который
вы пытались запустить, запустится без этого меню.
                   """)


    def reboot_bsod():
        script_path = os.path.abspath(__file__)
        subprocess.Popen(
            ["cmd", "/c", sys.executable, str(script_path)],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        sys.exit()
        root.destroy()



    def install_pip_cmd():
        label_ru.config(text=f"Подождите..", fg="white")
        label_ru.pack(anchor="nw", pady=5)
        label_eng.config(text=f"Wait..", fg="white")
        label_eng.pack(anchor="nw", pady=5)
        if e.name == "PIL":
            subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"])
            return
        try:
            result = subprocess.run([sys.executable, "-m", "pip", "install", e.name], capture_output=True, text=True)
            if result.returncode == 0:
                label_ru.config(text=f"pip {e.name} Установлено!", fg="#00CF00")
                label_ru.pack(anchor="nw", pady=5)
                label_eng.config(text=f"pip {e.name} it was established", fg="green")
                label_eng.pack(anchor="nw", pady=5)

            if result.returncode != 0:
                error_msg = result.stderr
                label_ru.config(text=f"Ошибка pip: {error_msg}", fg="red")
                label_ru.pack(anchor="nw", pady=5)
                label_eng.config(text=f"error pip: {error_msg}", fg="red")
                label_eng.pack(anchor="nw", pady=5)


        except Exception as error_pip_cmd:
           print(error_pip_cmd)

    def upd_pip_cmd():
        label_pipudp.config(text="wait...")
        label_pipudp.pack(anchor="sw", pady=5, padx=20)
        try:
            result = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], capture_output=True, text=True)
            if result.returncode == 0:
                out_msg = result.stdout
                label_pipudp.config(text=f"pip successfully updated\n{out_msg}", fg="#00CF00")
                label_pipudp.pack(anchor="sw", pady=5, padx=20)
            if result.returncode != 0:
                error_msg = result.stderr
                label_pipudp.config(text=f"pip upd error: {error_msg}", fg="red")
                label_pipudp.pack(anchor="sw", pady=5, padx=20)

        except Exception as error_updpip:
            print(error_updpip)


    def thread_install_pip_cmd():
        threading.Thread(target=install_pip_cmd).start()

    def thread_upd_pip_cmd():
        threading.Thread(target=upd_pip_cmd).start()


    def fullscreen_on():
        global fullscreen
        fullscreen = not fullscreen

        if fullscreen:
            root.attributes('-fullscreen', True)
        else:
            root.attributes('-fullscreen', False)
            root.geometry("960x540")

    bg_state = 1
    def theme_tk():
        global bg_state

        if bg_state == 1:
            #blacck
            for frames in (frame, frame2, root, info_frame):
                frames.config(bg="black")
                for widget in frames.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(
                            bg="#0A0A0A",
                            activebackground="#0F0F0F",
                            activeforeground="white"
                        )
                for labels in frames.winfo_children():
                    if isinstance(labels, tk.Label):
                        labels.config(
                            bg="black",
                        )
            bg_state = 2
        elif bg_state == 2:
            #white
            for frames in (frame, frame2, root, info_frame):
                frames.config(bg="white")
                for widget in frames.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(
                            bg="#EBEBEB",
                            activebackground="#C3C3C3",
                            fg="black",
                            activeforeground = "black"
                        )
                for labels in frames.winfo_children():
                    if isinstance(labels, tk.Label):
                        labels.config(
                            bg="white",
                            fg="black"
                        )
            bg_state = 3
        else:
            #blue
            for frames in (frame, frame2, root, info_frame):
                frames.config(bg="blue")
                for widget in frames.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(
                            bg="blue",
                            activebackground="#0010A7",
                            fg="white",
                            activeforeground="white",
                        )
                for labels in frames.winfo_children():
                    if isinstance(labels, tk.Label):
                        labels.config(
                            bg="blue",
                            fg="white"
                        )
            bg_state = 1


    frame = tk.Frame(root, bg="blue")
    frame.pack(padx=20, anchor="nw")
    frame2 = tk.Frame(root, bg="blue")
    frame2.pack(padx=20, anchor="nw")
    info_frame = tk.Frame(root, bg="blue")
    info_frame.pack(side="right", pady=20, padx=20, anchor="se")


    btnfullscr = tk.Button(frame2, text="Fullscreen", activebackground="#0010A7", bg="blue", fg="white", command=fullscreen_on, width=10)
    btnfullscr.pack(side="left", padx=5, pady=5)

    theme_btn = tk.Button(frame2, text="Theme", activebackground="#0010A7", bg="blue", fg="white", command=theme_tk, width=10)
    theme_btn.pack(side="left", padx=5, pady=5)


    label_time = tk.Label(info_frame, text=f"{data1} {time1}", fg="white", bg="blue", font=("bold", 12))
    label_time.pack(pady=10)

    label_help = tk.Label(info_frame, text=text, fg="white", bg="blue", font=("bold", 12))
    label_help.pack(pady=10)

    labelinfo = tk.Label(info_frame, text=f"version: {pyver}\ncompiler: {pycomp}\nbuild: {pybuild}", fg="white", bg="blue", font=("bold", 15))
    labelinfo.pack(pady=5)

    label_ru = tk.Label(frame, fg="white", bg="blue", font=("bold", 15), text=f"Отсутствующие модули: {e.name}", justify="left", anchor="nw")
    label_ru.pack(anchor="nw", pady=5)

    label_eng = tk.Label(frame, fg="white", bg="blue", font=("bold", 15), text=f"Missing modules: {e.name}",justify="left", anchor="nw")
    label_eng.pack(anchor="nw", pady=5)

    label_pipudp = tk.Label(root, fg="white", bg="blue", font=("bold", 15), text=f"", justify="left", anchor="sw")

    btn_exit = tk.Button(frame, text="Exit", activebackground="#0010A7", bg="blue", fg="white", command=exit_bbt, width=10)
    btn_exit.pack(side="left", padx=5, pady=5)

    btn_reboot = tk.Button(frame, text="Reboot", activebackground="#0010A7", bg="blue", fg="white", command=reboot_bsod, width=10)
    btn_reboot.pack(side="left", padx=5, pady=5)

    btn_download = tk.Button(frame, text="Install", activebackground="#0010A7", bg="blue", fg="white", command=thread_install_pip_cmd, width=10)
    btn_download.pack(side="left", padx=5, pady=5)

    btn_pip = tk.Button(frame, text="upgrade pip", activebackground="#0010A7", bg="blue", fg="white", command=thread_upd_pip_cmd, width=10)
    btn_pip.pack(side="left", padx=5, pady=5)

    root.mainloop()