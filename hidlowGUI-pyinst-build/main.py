import subprocess
import sys
import os
from pathlib import Path
import threading
import ctypes
import json
import customtkinter as ctk
from PIL import Image, ImageTk

#messagebox
def msgb(text, title):
    threading.Thread(target=lambda: ctypes.windll.user32.MessageBoxW(0, text, title, 0x10), daemon=True).start()


# for pyinstaller
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.normpath(os.path.join(base_path, relative_path.replace('/', os.sep)))

class Subprocess_scripts:
    def __init__(self):
        self.check_troll = Path(resource_path(r"files/troll"))
        self.scr_troll = self.check_troll / "trollhidlowGUI.py"

        self.files_dir = Path(resource_path(r"files"))
        self.scr_flask = self.files_dir / "hidlowAPI.py"

        self.check_debug = Path(resource_path(r"files/consoledebug"))
        self.scr_debug = self.check_debug / "debugconsole.py"

        self.scr_winsize = self.files_dir / "window_size.py"

    def trol(self):
        try:
            if self.scr_troll.exists():
                try:
                    subprocess.Popen(["py", str(self.scr_troll)], cwd=str(self.check_troll))
                except Exception:
                    try:
                        subprocess.Popen(["python", str(self.scr_troll)], cwd=str(self.check_troll))
                    except Exception:
                        msgb("Python not found\nInstall python for run script", "troll error")
            else:
                msgb("Ошибка открытия TrollGUI\nПроверьте совместимость сборки", "HidlowToolsGUI")
        except Exception as error_troll_cmd:
            msgb(f"{error_troll_cmd}", "HidlowToolsGUI-error")

    # HidlowAPI
    def hidlowapi_cmd(self):
        try:
            if self.scr_flask.exists():
                try:
                    subprocess.Popen(["py", str(self.scr_flask)], cwd=str(self.files_dir), creationflags=subprocess.CREATE_NEW_CONSOLE)
                except Exception:
                    try:
                        subprocess.Popen(["python", str(self.scr_flask)], cwd=str(self.files_dir), creationflags=subprocess.CREATE_NEW_CONSOLE)
                    except Exception:
                        msgb("Python not found\nInstall python for run script", "flask error")
            else:
                msgb("Ошибка запуска HidlowAPI\nПроверьте совместимость сборки", "HidlowToolsGUI")
        except Exception as error_api_cmd:
            msgb(f"{error_api_cmd}", "HidlowToolsGUI-error")

    def winsize(self):
        try:
            if self.scr_winsize.exists():
                try:
                    subprocess.Popen(["py", str(self.scr_winsize)], cwd=str(self.files_dir))
                except Exception:
                    try:
                        subprocess.Popen(["python", str(self.scr_winsize)], cwd=str(self.files_dir))
                    except Exception:
                        msgb("Python not found\nInstall python for run script", "winsize error")
            else:
                msgb("Ошибка запуска WinSize\nПроверьте совместимость сборки", "HidlowToolsGUI")
        except Exception as error_wns_cmd:
            msgb(f"{error_wns_cmd}", "HidlowToolsGUI-error")

    # console
    def consoleadapter(self):
        try:
            if self.scr_debug.exists():
                try:
                    subprocess.Popen(["py", str(self.scr_debug)], cwd=str(self.check_debug), creationflags=subprocess.CREATE_NEW_CONSOLE)
                except Exception:
                    try:
                        subprocess.Popen(["python", str(self.scr_debug)], cwd=str(self.check_debug), creationflags=subprocess.CREATE_NEW_CONSOLE)
                    except Exception:
                        msgb("Python not found\nInstall python for run script", "debug error")
            else:
                msgb(f'Сборка повреждена\nКонсоль недоступна\nПроверьте совместимость сборки', 'debug-console')
        except Exception as error_prepare_console:
            msgb(f"{error_prepare_console}", "debug-console-error")


class Logic:
    def __init__(self, main):
        self.main = main

    def select_api1(self):
        from files.number_api_util import Api
        api = Api(self.main.output_label)
        self.clear_entry_frame()
        self.prepare_input(lambda: api.api_number(self.main.entry, self.main.output_label, self.main.root, self.main.copy_btn, self.main.confirm_button, self.main.back_button, self.main.clear_btn, self.main.paste_btn))

    # ip api util
    def select_api2(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        self.clear_entry_frame()
        self.prepare_input(lambda: api.api_ip(self.main.entry, self.main.output_label, self.main.root, self.main.copy_btn, self.main.confirm_button, self.main.back_button, self.main.clear_btn, self.main.paste_btn))

    # geo api util
    def select_api3(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        self.clear_entry_frame()
        self.prepare_input(lambda: api.api_lat(self.main.entry, self.main.output_label, self.main.root, self.main.copy_btn, self.main.confirm_button, self.main.back_button, self.main.clear_btn, self.main.paste_btn))

    # prepare spawn currency-frame
    def select_currency(self):
        self.main.menu_frame.place_forget()
        self.main.currency_frame.place(x=1, y=1)

    # prepare util
    def ton_pr(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        api.select_ton(self.main.root)

    # prepare util
    def btc_pr(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        api.select_btc(self.main.root)

    # prepare util
    def select_gptchc(self):
        from files.none_textbox_utils import Utils
        self.clear_entry_frame()
        scr = Utils(self.main.output_label)
        self.prepare_input(lambda: scr.gpthch(self.main.entry, self.main.output_label, self.main.extra_label))

    # prepare spawn faker-frame
    def select_faker(self):
        self.main.menu_frame.place_forget()
        self.main.faker_frame.place(x=1, y=1)

    def faker_ru_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.place_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.place_forget()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_ru(self.main.faker_frame)

    # prepare faker eng
    def faker_eng_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.place_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.place_forget()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_eng(self.main.faker_frame)

    # prepare faker spain
    def faker_es_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.place_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.place_forget()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_es(self.main.faker_frame)

    # prepare faker japanese
    def faker_jp_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.place_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.place_forget()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_jp(self.main.faker_frame)

    # prepare util
    def select_qrcode(self):
        from files.none_textbox_utils import Utils

        scr = Utils(self.main.output_label)
        self.prepare_input(lambda: scr.qrcodee(self.main.entry, self.main.output_label))

    # prepare util
    def select_notify(self):
        from files.none_textbox_utils import Utils
        scr = Utils(self.main.output_label)
        self.main.menu_frame.place_forget()
        self.prepare_input(lambda: scr.ctypes_notify(self.main.entry, self.main.output_label))

    # prepare monitoring util
    def select_monitor(self):
        from files.monitoring_util import Util
        scr = Util(self.main.label_mon, self.main.label_mem, self.main.label_cpu, self.main.label_info_monitor)
        self.main.menu_frame.place_forget()
        self.main.monitor_frame.place(x=1, y=1)
        threading.Thread(target=lambda: scr.monitoring_start(
            self.main.label_mon, self.main.label_mem, self.main.label_cpu, self.main.label_info_monitor), daemon=True).start()

    # prepare entry
    def prepare_input(self, api_func):
        self.main.menu_frame.place_forget()
        self.clear_entry_frame()
        self.main.entry_frame.place(x=1, y=1)
        self.input_clear()
        self.main.confirm_button.configure(command=lambda: threading.Thread(target=api_func, daemon=True).start())

    def paste(self):
        paste_text = self.main.root.clipboard_get()
        self.main.entry.delete(0, ctk.END)
        self.main.entry.insert(0, paste_text)

    def go_back(self, hide_frame):
        # основная функция выхода в главное меню
        hide_frame.place_forget()
        for widget in self.main.root.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                self.main.extra_label.pack_forget()
                widget.place_forget()
        self.main.menu_frame.place(x=1, y=1)

    def go_back_from_entry(self):
        # выход из entry-фрейма в главное меню
        self.main.entry_frame.place_forget()
        for widget in self.main.root.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                self.main.extra_label.pack_forget()
                widget.place_forget()
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        self.main.menu_frame.place(x=1, y=1)

    def go_back_monitoring(self):
        # выход из monitoring в главное меню
        self.main.monitor_frame.place_forget()
        self.main.menu_frame.place(x=1, y=1)

    def go_back_currency(self):
        for widget in self.main.root.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        self.go_back(self.main.currency_frame)

    def toggle_settings(self):
        if self.main.settings_frame.winfo_ismapped():
            self.main.settings_frame.place_forget()
            self.main.menu_frame.place(x=1, y=1)
        else:
            self.main.menu_frame.place_forget()
            self.main.settings_frame.place(x=1, y=1)

    def clear_entry_frame(self):
        # очиста ввода
        self.main.entry.delete(0, "end")
        for widget in self.main.entry_frame.winfo_children():
            if isinstance(widget, ctk.CTkTextbox):
                widget.place_forget()

    def input_clear(self):
        self.main.entry.delete(0, "end")
        for widget in self.main.root.winfo_children():
            if isinstance(widget, ctk.CTkTextbox):
                widget.pack_forget()
        self.main.copy_btn.configure(text_color="white")
        self.main.clear_btn.place_forget()
        self.main.entry.place(x=270, y=10)
        self.main.confirm_button.place(x=340, y=50)
        self.main.back_button.place(x=400, y=50)
        self.main.paste_btn.place(x=340, y=90)
        self.main.copy_btn.place(x=400, y=90)


class Main:
    def __init__(self, master):
        super().__init__()
        self.bg_state = 1
        self.found_cache = False
        self.folder_dir = os.path.dirname(os.path.abspath(__file__))
        self.default_theme = {"theme": "dark"}
        try:
            if not os.path.exists('settings.json'):
                with open("settings.json", "w", encoding="utf-8") as f:
                    json.dump(self.default_theme, f)

            with open('settings.json', 'r', encoding='utf-8') as f:
                self.th_data = json.load(f)
        except Exception as err_js:
            msgb(f"{err_js}", "json-error")

        self.root = master
        self.root.resizable(False, False)
        root.geometry("786x461")
        root.title("HidlowTools-GUI-V2")
        self.root.configure(fg_color="#1A1A1A")
        ctk.set_appearance_mode("Dark")

        self.cli_files = Subprocess_scripts()
        self.prepare = Logic(self)

        get_exit_btn = resource_path("assets/exit_assets/exitbutton1.png")
        try:
            self.exit_buttons = [ctk.CTkImage(light_image=Image.open(get_exit_btn).resize((27, 27)), size=(27, 27))]
        except Exception as b:
            msgb(f"{b}", "bg-error")

        self._widgets()
        self.load_theme()


    def _widgets(self):
        # главное меню
        self.menu_frame = ctk.CTkFrame(self.root, fg_color="#1A1A1A", width=780)
        self.menu_frame.place(x=1, y=1)

        # главное меню №2
        self.off_menu = ctk.CTkFrame(self.root, fg_color="#1A1A1A", width=80, height=300)
        self.off_menu.place(x=1, y=220)

        # settigs frame
        self.settings_frame = ctk.CTkFrame(self.root, fg_color="#1A1A1A")

        # currency frame
        self.currency_frame = ctk.CTkFrame(self.root, fg_color="#1A1A1A", width=780, height=600)

        # faker frame
        self.faker_frame = ctk.CTkFrame(self.root, fg_color="#1A1A1A", width=780, height=500)

        # monitor frame
        self.monitor_frame = ctk.CTkFrame(self.root, fg_color="#1A1A1A", width=780, height=500)

        # кнопки
        self.button1 = ctk.CTkButton(self.menu_frame, text="Number", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command= self.prepare.select_api1).place(x=10, y=10)
        self.button2 = ctk.CTkButton(self.menu_frame, text="IP", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_api2).place(x=90, y=10)
        self.button3 = ctk.CTkButton(self.menu_frame, text="GEO", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_api3).place(x=168, y=10)
        self.button4 = ctk.CTkButton(self.menu_frame, text="Currency", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_currency).place(x=248, y=10)

        self.button5 = ctk.CTkButton(self.menu_frame, text="Troll", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.cli_files.trol).place(x=10, y=50)
        self.button6 = ctk.CTkButton(self.menu_frame, text="API", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.cli_files.hidlowapi_cmd).place(x=90, y=50)
        self.button6_1 = ctk.CTkButton(self.menu_frame, text="WinSize", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.cli_files.winsize).place(x=168, y=50)

        self.button7 = ctk.CTkButton(self.menu_frame, text="Faker", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_faker).place(x=10, y=90)
        self.button8 = ctk.CTkButton(self.menu_frame, text="QRcode", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_qrcode).place(x=90, y=90)
        self.button9 = ctk.CTkButton(self.menu_frame, text="GPT CHC", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_gptchc).place(x=168, y=90)

        self.button10 = ctk.CTkButton(self.menu_frame, text="Notify", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_notify).place(x=10, y=130)
        self.button11 = ctk.CTkButton(self.menu_frame, text="Psutil", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.select_monitor).place(x=90, y=130)

        self.settings_button = ctk.CTkButton(self.menu_frame, text="Settings", text_color="white", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.toggle_settings).place(x=710, y=10)
        self.about_btn = ctk.CTkButton(self.menu_frame, text="Info", text_color="white", width=70, corner_radius=5, fg_color="#242424", hover_color="#141414", command=lambda: os.system("start https://github.com/hiikikomorii/hidlowToolsGUI")).place(x=711, y=50)

        # buttons in settings
        self.btn2 = ctk.CTkButton(self.settings_frame, text="Theme", text_color="white", width=90, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.change_background).place(x=10, y=10)
        self.btn3 = ctk.CTkButton(self.settings_frame, text="Clear cache", text_color="white", width=90, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.clear_cache)
        self.btn3.place(x=10, y=50)
        self.btn4 = ctk.CTkButton(self.settings_frame, text="Folder", text_color="white", width=90, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.open_folder).place(x=10, y=90)
        self.btn5 = ctk.CTkButton(self.settings_frame, text="Debug", text_color="white", width=90, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.cli_files.consoleadapter).place(x=10, y=130)
        self.back_stng = ctk.CTkButton(self.settings_frame, text="Back", text_color="red", width=90, corner_radius=5, fg_color="#242424", hover_color="#141414", command=self.prepare.toggle_settings)
        self.back_stng.place(x=10, y=170)


        self.exitadapter_button = ctk.CTkButton(self.off_menu, text="", image=self.exit_buttons[0], fg_color="transparent", corner_radius=0, width=10, command=lambda: self.root.destroy())
        self.exitadapter_button.place(x=10, y=190)

        # ввод
        self.entry_frame = ctk.CTkFrame(self.root, width=900, height=500, fg_color="#1A1A1A")
        self.entry = ctk.CTkEntry(self.entry_frame, width=250)
        self.entry.place(x=270, y=10)

        self.confirm_button = ctk.CTkButton(self.entry_frame, text="OK", fg_color="#242424", hover_color="#141414", corner_radius=5, text_color="#00CF00", width=50)
        self.confirm_button.place(x=340, y=50)

        self.back_button = ctk.CTkButton(self.entry_frame, text="Back", fg_color="#242424", hover_color="#141414", corner_radius=5, text_color="red", width=50, command=self.prepare.go_back_from_entry)
        self.back_button.place(x=400, y=50)

        self.paste_btn = ctk.CTkButton(self.entry_frame, text="Paste", fg_color="#242424", hover_color="#141414", corner_radius=5, width=50, command=self.prepare.paste)
        self.paste_btn.place(x=340, y=90)

        self.copy_btn = ctk.CTkButton(self.entry_frame, text="Copy", fg_color="#242424", hover_color="#141414", corner_radius=5, width=50)
        self.copy_btn.place(x=400, y=90)

        self.clear_btn = ctk.CTkButton(self.entry_frame, text="Clear", fg_color="#242424", hover_color="#141414", corner_radius=5, width=50, command=self.prepare.input_clear)


        # currency
        self.btc_button = ctk.CTkButton(self.currency_frame, text="BTC", text_color="white", fg_color="#242424", hover_color="#141414", corner_radius=5, width=60, command=self.prepare.btc_pr).place(x=10, y=10)
        self.ton_button = ctk.CTkButton(self.currency_frame, text="TON", text_color="white", fg_color="#242424", hover_color="#141414", corner_radius=5, width=60, command=self.prepare.ton_pr).place(x=10, y=50)
        self.currencyback_button = ctk.CTkButton(self.currency_frame, text="Back", text_color="red", fg_color="#242424", hover_color="#141414", corner_radius=5, width=60, command=self.prepare.go_back_currency)
        self.currencyback_button.place(x=10, y=90)

        # faker
        self.rubtn = ctk.CTkButton(self.faker_frame, text="Russian", text_color="white", fg_color="#242424", hover_color="#141414", corner_radius=5, width=80, command=self.prepare.faker_ru_pr).place(x=10, y=10)
        self.engbtn = ctk.CTkButton(self.faker_frame, text="English", text_color="white", fg_color="#242424", hover_color="#141414", corner_radius=5, width=80, command=self.prepare.faker_eng_pr).place(x=10, y=50)
        self.kzbtn = ctk.CTkButton(self.faker_frame, text="Spanish", text_color="white", fg_color="#242424", hover_color="#141414", corner_radius=5, width=80, command=self.prepare.faker_es_pr).place(x=10, y=90)
        self.jpbtn = ctk.CTkButton(self.faker_frame, text="Japanese", text_color="white", fg_color="#242424", hover_color="#141414", corner_radius=5, width=80, command=self.prepare.faker_jp_pr).place(x=10, y=130)
        self.fakerback_button = ctk.CTkButton(self.faker_frame, text="Back", text_color="red", fg_color="#242424", hover_color="#141414", corner_radius=5, width=80, command=lambda: self.prepare.go_back(self.faker_frame))
        self.fakerback_button.place(x=10, y=170)

        # monitor
        self.label_mon = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 17))
        self.label_mem = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 17))
        self.label_cpu = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 17))
        self.label_info_monitor = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 15))
        self.monitorback_button = ctk.CTkButton(self.monitor_frame, text="Back", fg_color="#242424", hover_color="#141414", corner_radius=5, text_color="red", width=70, command=self.prepare.go_back_monitoring)
        self.monitorback_button.place(x=10, y=425)

        # labels
        self.output_label = ctk.CTkLabel(self.root, text_color="#FF0000")
        self.extra_label = ctk.CTkLabel(self.root, text_color="#FF0000")
        self.copyable = ctk.CTkTextbox(self.root)

    def open_folder(self):
        # открывает директорию в котором находится main.py
        try:
            os.startfile(self.folder_dir)
        except Exception as error_folder:
            msgb(f"{__file__}'\n{error_folder}", "folder-error")

    def clear_cache(self):
        # очистка __pycache__
        import shutil

        for wroot, dirs, files in os.walk(self.folder_dir):
            if '__pycache__' in dirs:
                cache_path = os.path.join(wroot, '__pycache__')
                shutil.rmtree(cache_path)
                msgb(f"cache deleted\n{cache_path}", "Cache")
                self.btn3.configure(text_color="#00CF00")
                self.found_cache = True
                return

        if not self.found_cache:
            self.btn3.configure(text_color="#00CF00")
        else:
            self.btn3.configure(text_color="#00CF00")

    def load_theme(self):
        if self.th_data["theme"] == "light":
            self.bg_state = 1
            self.change_background()

        if self.th_data["theme"] == "dark":
            self.bg_state = 2
            self.change_background()


    def change_background(self):
        if self.bg_state == 1:
            # white
            try:
                for frame1 in (self.root, self.menu_frame, self.off_menu, self.settings_frame, self.currency_frame, self.entry_frame, self.faker_frame, self.monitor_frame):
                    frame1.configure(fg_color="#EBEBEB")
                self.exitadapter_button.configure(hover_color="#EBEBEB", border_color="#EBEBEB")

                for labels_wid in self.monitor_frame.winfo_children():
                    if isinstance(labels_wid, ctk.CTkLabel):
                        labels_wid.configure(text_color="black")

                for light_th in (self.menu_frame, self.settings_frame, self.currency_frame, self.entry_frame, self.faker_frame, self.monitor_frame):
                    for widget in light_th.winfo_children():
                        if isinstance(widget, ctk.CTkButton):
                            widget.configure(fg_color="#C2C2C2", hover_color="#8F8F8F", text_color="#3D3D3D")

                        for b in (self.back_stng, self.back_button, self.currencyback_button, self.fakerback_button, self.monitorback_button):
                            b.configure(text_color="red")
                self.th_data["theme"] = "light"
                with open("settings.json", "w", encoding="utf-8") as ed:
                    json.dump(self.th_data, ed, indent=4, ensure_ascii=False)

            except Exception as a:
                msgb(f"{a}", "bg-light-mode")

            self.bg_state = 2

        else:
            # black
            try:
                for frame in (self.root, self.menu_frame, self.off_menu, self.settings_frame,
                              self.currency_frame, self.entry_frame, self.faker_frame, self.monitor_frame):
                    frame.configure(fg_color="#1A1A1A")

                for labels_wid in self.monitor_frame.winfo_children():
                    if isinstance(labels_wid, ctk.CTkLabel):
                        labels_wid.configure(text_color="white")

                for light_th in (self.menu_frame, self.settings_frame, self.currency_frame, self.entry_frame, self.faker_frame, self.monitor_frame):
                    for widget in light_th.winfo_children():
                        if isinstance(widget, ctk.CTkButton):
                            widget.configure(fg_color="#242424", hover_color="#141414", text_color="white")

                        self.exitadapter_button.configure(hover_color="#1A1A1A")

                        for b in (self.back_stng, self.back_button, self.currencyback_button, self.fakerback_button,
                                  self.monitorback_button):
                            b.configure(text_color="red")

                self.th_data["theme"] = "dark"
                with open("settings.json", "w", encoding="utf-8") as ed:
                    json.dump(self.th_data, ed, indent=4, ensure_ascii=False)

            except Exception as a:
                msgb(f"{a}", "bg-dark-mode")
            self.bg_state = 1



if __name__ == '__main__':
    root = ctk.CTk()
    app = Main(root)
    root.mainloop()
