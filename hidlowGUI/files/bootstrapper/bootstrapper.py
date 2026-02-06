import subprocess
import sys
import tkinter as tk
import os
import threading
from datetime import date, datetime

def log(text):
    time_log = datetime.now().strftime("%H:%M:%S")
    date_log = date.today()
    with open("BOOTLOG.txt", "a", encoding="utf-8") as file:
        file.write(f"[{date_log} | {time_log}] {text}\n")

class Pip:
    def __init__(self, label_eng, label_pipudp, main):
        self.label_eng = label_eng
        self.label_pipudp = label_pipudp
        self.main = main

    def install_pip_cmd(self):
        self.label_eng.config(text=f"Wait..", fg="white")
        self.label_eng.pack(anchor="nw", pady=5)

        if self.main.missing_module_name == "PIL":
            result = subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"])
            if result.returncode == 0:
                self.label_eng.config(text=f"pip {self.main.missing_module_name} it was established", fg="#00CF00")
                self.label_eng.pack(anchor="nw", pady=5)
                log(f"[PIP INSTALL] {result}")
                self.main.download_pip = True

            if result.returncode != 0:
                error_msg = result.stderr
                self.label_eng.config(text=f"error pip: {error_msg}", fg="red")
                self.label_eng.pack(anchor="nw", pady=5)
                log(f"[PIP INSTALL] {error_msg}")
            return

        try:
            result = subprocess.run([sys.executable, "-m", "pip", "install", self.main.missing_module_name], capture_output=True, text=True)
            if result.returncode == 0:
                self.label_eng.config(text=f"pip {self.main.missing_module_name} it was established", fg="#00CF00")
                self.label_eng.pack(anchor="nw", pady=5)
                log(f"[PIP] pip {self.main.missing_module_name} it was established")
                self.main.download_pip = True

            if result.returncode != 0:
                error_msg = result.stderr
                self.label_eng.config(text=f"error pip: {error_msg}", fg="red")
                self.label_eng.pack(anchor="nw", pady=5)
                log(f"[PIP] {error_msg}")

        except Exception as error_pip_cmd:
            print(error_pip_cmd)

    def upd_pip_cmd(self):
        self.label_pipudp.config(text="wait...")
        self.label_pipudp.pack(anchor="sw", pady=5, padx=20)
        try:
            result = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], capture_output=True, text=True)
            if result.returncode == 0:
                out_msg = result.stdout
                self.label_pipudp.config(text=f"pip successfully updated\n{out_msg}", fg="#00CF00")
                self.label_pipudp.pack(anchor="sw", pady=5, padx=20)
                log(f"[PIP UPDATE] pip successfully updated")
                self.main.update_pip = True

            if result.returncode != 0:
                error_msg = result.stderr
                self.label_pipudp.config(text=f"pip upd error: {error_msg}", fg="red")
                self.label_pipudp.pack(anchor="sw", pady=5, padx=20)
                log(f"[PIP UPDATE] {error_msg}")

        except Exception as error_updpip:
            print(error_updpip)


class Main:
    def __init__(self, master):
        import platform
        try:
            os.remove("BOOTLOG.txt")
        except FileNotFoundError:
            pass

        self.missing_module_name = "none"

        self.bg_state = 1
        self.fullscreen = False
        self.download_pip = False
        self.update_pip = False
        self.reboot_path = os.path.abspath(__file__)

        self.text = ("""
        Bootstrapped-menu\n
        Script startup failed.
        Install: Download missing modules.
        Upgrade pip: Update pip to the latest version.
        Reboot: Restart the script.
        The script will bypass this menu if it runs successfully.""")

        try:
            self.check_pip()
        except Exception:
            pass

        self.root = master
        self.root.title("BOOTSTRAPPER-NOMODULE")
        self.root.config(bg="blue")
        self.root.geometry("976x635")

        self.pybuild = platform.python_build()
        self.pycomp = platform.python_compiler()
        self.pyver = platform.python_version()
        self._all_widgets()
        self.use_pip = Pip(self.label_eng, self.label_pipudp, self)

    def _all_widgets(self):
        self.frame = tk.Frame(self.root, bg="blue")
        self.frame.pack(padx=20, anchor="nw")

        self.frame2 = tk.Frame(self.root, bg="blue")
        self.frame2.pack(padx=20, anchor="nw")

        self.settings_frame = tk.Frame(self.root, bg="blue")

        self.info_frame = tk.Frame(self.root, bg="blue")
        self.info_frame.pack(side="right", pady=20, padx=20, anchor="se")

        self.btnfullscr = tk.Button(self.settings_frame, text="Fullscreen", activebackground="#0010A7", bg="blue", fg="white",command=self.fullscreen_on, width=10)

        self.theme_btn = tk.Button(self.settings_frame, text="Theme", activebackground="#0010A7", bg="blue", fg="white", command=self.theme_tk, width=10)

        self.back_settings_btn = tk.Button(self.settings_frame, text="Back", activebackground="#0010A7", bg="blue", fg="red", command=self.back_settings, width=10)

        self.label_help = tk.Label(self.info_frame, text=self.text, fg="white", bg="blue", font=("bold", 15))
        self.label_help.pack(pady=10)

        self.labelinfo = tk.Label(self.info_frame, text=f"version: {self.pyver}\ncompiler: {self.pycomp}\nbuild: {self.pybuild}", fg="white", bg="blue", font=("bold", 15))
        self.labelinfo.pack(pady=5)

        self.label_eng = tk.Label(self.frame, fg="white", bg="blue", font=("bold", 15), text=f"Missing modules: {self.missing_module_name}", justify="left", anchor="nw")
        self.label_eng.pack(anchor="nw", pady=5)

        self.label_pipudp = tk.Label(self.root, fg="white", bg="blue", font=("bold", 15), text=f"", justify="left", anchor="sw")

        self.btn_exit = tk.Button(self.frame, text="Exit", activebackground="#0010A7", bg="blue", fg="white", command=lambda: sys.exit(0), width=10)
        self.btn_exit.pack(side="left", padx=5, pady=5)

        self.btn_reboot = tk.Button(self.frame, text="Reboot", activebackground="#0010A7", bg="blue", fg="white", command=self.reboot_bsod, width=10)
        self.btn_reboot.pack(side="left", padx=5, pady=5)

        self.btn_download = tk.Button(self.frame2, text="Install", activebackground="#0010A7", bg="blue", fg="white", command=lambda: threading.Thread(target=self.use_pip.install_pip_cmd).start(),width=10)
        self.btn_download.pack(side="left", padx=5, pady=7)

        self.btn_pip = tk.Button(self.frame2, text="upgrade pip", activebackground="#0010A7", bg="blue", fg="white", command=lambda: threading.Thread(target=self.use_pip.upd_pip_cmd).start(), width=10)
        self.btn_pip.pack(side="left", padx=5, pady=7)

        self.settings_btn = tk.Button(self.frame, text="Settings", activebackground="#0010A7", bg="blue", fg="white", command=self.settings, width=10)
        self.settings_btn.pack(side="left", padx=5, pady=5)


    def check_pip(self):
        try:
            import asdasdasd
            import customtkinter
            import colorama
            import requests
            from PIL import Image, ImageTk
            import phonenumbers
            from faker import Faker
            import pygetwindow
            import psutil
            import pynput
            import qrcode
            from flask import Flask, jsonify

            log("[SUCCESS] All modules are installed")
            hidlow_path = "main.py"
            subprocess.Popen(
                ["cmd", "/k", sys.executable, str(hidlow_path)],
                cwd="../../",
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )

            sys.exit()
        except ModuleNotFoundError as e:
            self.missing_module_name = e.name
            log(f"[ERROR] missing module: {self.missing_module_name}")

    def reboot_bsod(self):
        subprocess.Popen(
            ["cmd", "/c", sys.executable, str(self.reboot_path)],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        sys.exit()
        self.root.destroy()

    def fullscreen_on(self):
        self.fullscreen = not self.fullscreen

        if self.fullscreen:
            self.root.attributes('-fullscreen', True)
            log("[INFO] fullscreen ON")
        else:
            self.root.attributes('-fullscreen', False)
            self.root.geometry("976x635")
            log("[INFO] fullscreen OFF")

    def settings(self):
        for btns in (self.frame, self.frame2):
            for b in btns.winfo_children():
                if isinstance(b, tk.Button):
                    b.pack_forget()
        self.frame2.pack_forget()
        self.settings_frame.pack(padx=20, anchor="nw")
        self.back_settings_btn.pack(side="left", padx=5, pady=5)
        self.theme_btn.pack(side="left", padx=5, pady=5)
        self.btnfullscr.pack(side="left", padx=5, pady=5)

    def back_settings(self):
        self.settings_frame.pack_forget()
        self.frame2.pack(padx=20, anchor="nw")
        for btns in (self.frame, self.frame2):
            for b in btns.winfo_children():
                if isinstance(b, tk.Button):
                    b.pack(side="left", padx=5, pady=5)

    def theme_tk(self):
        if self.bg_state == 1:
            # black
            for frames in (self.settings_frame, self.frame, self.frame2, self.root, self.info_frame):
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

            self.bg_state = 2
        elif self.bg_state == 2:
            # white
            for frames in (self.settings_frame, self.frame, self.frame2, self.root, self.info_frame):
                frames.config(bg="white")

                for widget in frames.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(
                            bg="#EBEBEB",
                            activebackground="#C3C3C3",
                            fg="black",
                            activeforeground="black"
                        )
                        self.back_settings_btn.config(fg="red")

                for labels in frames.winfo_children():
                    if isinstance(labels, tk.Label):
                        labels.config(
                            bg="white",
                            fg="black"
                        )
                        if self.download_pip:
                            self.label_ru.config(fg="#00CF00")
                            self.label_eng.config(fg="#00CF00")
                        if self.update_pip:
                            self.label_pipudp.config(fg="#00CF00")

            self.bg_state = 3
        else:
            # blue
            for frames in (self.settings_frame, self.frame, self.frame2, self.root, self.info_frame):
                frames.config(bg="blue")
                for widget in frames.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(
                            bg="blue",
                            activebackground="#0010A7",
                            fg="white",
                            activeforeground="white",
                        )
                        self.back_settings_btn.config(fg="red")

                for labels in frames.winfo_children():
                    if isinstance(labels, tk.Label):
                        labels.config(
                            bg="blue",
                            fg="white"
                        )
                        if self.download_pip:
                            self.label_ru.config(fg="#00CF00")
                            self.label_eng.config(fg="#00CF00")
                        if self.update_pip:
                            self.label_pipudp.config(fg="#00CF00")

            self.bg_state = 1


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

