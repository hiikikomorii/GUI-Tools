import subprocess
import sys
import os
from datetime import date, datetime
from pathlib import Path
import threading
import ctypes

try:
    import customtkinter as ctk
    from PIL import Image, ImageTk
    from colorama import init, Fore, Style

except ModuleNotFoundError as e:
    boot_path = "files/bootstrapper.py"
    subprocess.Popen(["cmd", "/c" , sys.executable, str(boot_path)],creationflags=subprocess.CREATE_NEW_CONSOLE)
    sys.exit()

init(autoreset=True)


class Subprocess_scripts:
    def __init__(self):
        self.check_troll = Path(r"files\troll\trollhidlowGUI.py")
        self.check_flask = Path(r"files\hidlowAPI.py")
        self.check_debug = Path(r"files\consoledebug\debugconsole.py")

    def trol(self):
        try:
            if self.check_troll.exists():
                print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} {Fore.MAGENTA}TrollGidlowGUI{Fore.RESET} | {Fore.LIGHTGREEN_EX}was opened")
                script_dir = Path(__file__).parent / "files" / "troll"
                script_file = script_dir / "trollhidlowGUI.py"
                subprocess.Popen(["cmd", "/c", sys.executable, str(script_file)], cwd=str(script_dir), creationflags=subprocess.CREATE_NEW_CONSOLE)

            else:
                ctypes.windll.user32.MessageBoxW(0, f"Ошибка открытия TrollGUI\nПроверьте совместимость сборки", "HidlowToolsGUI", 0x10)
        except Exception as error_troll_cmd:
            print(error_troll_cmd)

    # HidlowAPI
    def hidlowapi_cmd(self):
        try:
            if self.check_flask.exists():
                print(f"{Fore.BLUE}{Style.BRIGHT}[API Server]{Fore.RESET} {Fore.MAGENTA}HidlowAPI{Fore.RESET} | {Fore.LIGHTGREEN_EX}was enabled")
                script_dir = Path(__file__).parent / "files"
                script_file = script_dir / "hidlowAPI.py"
                subprocess.Popen(["cmd", "/c", sys.executable, str(script_file)], cwd=str(script_dir), creationflags=subprocess.CREATE_NEW_CONSOLE)

            else:
                ctypes.windll.user32.MessageBoxW(0, f"Ошибка запуска HidlowAPI\nПроверьте совместимость сборки", "HidlowToolsGUI", 0x10)
                print(f"{Fore.BLUE}{Style.BRIGHT}[API Server]{Style.NORMAL} {Fore.LIGHTRED_EX}Error")
        except Exception as error_api_cmd:
            print(error_api_cmd)

    # console
    def consoleadapter(self):
        try:
            if self.check_debug.exists():
                print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.MAGENTA}Debugconsole{Fore.RESET} | {Fore.LIGHTGREEN_EX}was opened")
                script_dir = Path(__file__).parent / "files" / "consoledebug"
                script_file = script_dir / "debugconsole.py"
                subprocess.Popen(["cmd", "/c", sys.executable, str(script_file)],cwd=str(script_dir), creationflags=subprocess.CREATE_NEW_CONSOLE)

            else:
                print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM] {Fore.RED}Debugconsole is not available\n")
                ctypes.windll.user32.MessageBoxW(0, f"Сборка повреждена\nКонсоль недоступна\nПроверьте совместимость сборки", "debug-console", 0x10)
        except Exception as error_prepare_console:
            print(error_prepare_console)

class Prepare_utils:
    def __init__(self, main):
        self.main = main

    def select_api1(self):
        from files.number_api_util import Api
        api = Api(self.main.output_label)
        self.clear_entry_frame()
        self.prepare_input(lambda: api.api_number(self.main.entry, self.main.output_label, self.main.textbox_frame, self.main.copy_btn))
        self.main.confirm_button.configure()
        self.main.back_button.configure()

    # ip api util
    def select_api2(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        self.clear_entry_frame()
        self.prepare_input(lambda: api.api_ip(self.main.entry, self.main.output_label, self.main.textbox_frame, self.main.copy_btn))

    # geo api util
    def select_api3(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        self.clear_entry_frame()
        self.prepare_input(lambda: api.api_lat(self.main.entry, self.main.output_label, self.main.textbox_frame, self.main.copy_btn))

    # prepare spawn currency-frame
    def select_currency(self):
        self.main.prepare_hide()
        self.main.currency_frame.pack(pady=10)

    # prepare util
    def ton_pr(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        api.select_ton(self.main.currency_frame)

    # prepare util
    def btc_pr(self):
        from files.main_api_utils import Api
        api = Api(self.main.copyable, self.main.output_label)
        api.select_btc(self.main.currency_frame)

    # prepare util
    def select_gptchc(self):
        from files.none_textbox_utils import Utils
        self.clear_entry_frame()
        scr = Utils(self.main.output_label)
        self.prepare_input(lambda: scr.gpthch(self.main.entry, self.main.output_label))

    # prepare spawn faker-frame
    def select_faker(self):
        self.main.prepare_hide()
        self.main.faker_frame.pack(pady=10)

    def faker_ru_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_ru(self.main.faker_frame)

    # prepare faker eng
    def faker_eng_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_eng(self.main.faker_frame)

    # prepare faker spain
    def faker_es_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        scr = Main_faker(self.main.faker_frame, self.main.copyable)
        scr.faker_es(self.main.faker_frame)

    # prepare faker japanese
    def faker_jp_pr(self):
        from files.faker_func import Main_faker
        for widget in self.main.faker_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
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
        self.main.prepare_hide()
        self.prepare_input(lambda: scr.ctypes_notify(self.main.entry, self.main.output_label))

    # prepare monitoring util
    def select_monitor(self):
        from files.monitoring_util import Util
        scr = Util(self.main.label_mon, self.main.label_mem, self.main.label_cpu, self.main.label_info_monitor)
        self.main.prepare_hide()
        self.main.monitor_frame.pack(padx=20)
        self.main.monitor_frame_stat.pack(side="left", anchor="sw", padx=20)
        threading.Thread(target=lambda: scr.monitoring_start(
            self.main.label_mon, self.main.label_mem, self.main.label_cpu, self.main.label_info_monitor), daemon=True).start()


    def select_about(self, about_frame):
        self.main.prepare_hide()
        about_frame.pack(pady=10)
        self.main.about_project()
        self.main.aboutback_button.configure(command=lambda: self.go_back(self.main.about_frame))

    # prepare entry
    def prepare_input(self, api_func):
        self.main.prepare_hide()
        self.clear_entry_frame()
        self.main.entry.pack(pady=5)
        self.main.entry_frame.pack(pady=10)
        self.main.ext_entry_frame.pack()
        self.main.confirm_button.configure(command=api_func)


    def go_back(self, hide_frame):
        # основная функция выхода в главное меню
        hide_frame.pack_forget()
        for widget in self.main.root.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.pack_forget()
        self.main.menu_frame.pack(pady=20)
        self.main.menu_frame2.pack(pady=20)

    def clear_entry_frame(self):
        # очиста ввода
        self.main.entry.delete(0, "end")
        for widget in self.main.entry_frame.winfo_children():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

class Main:
    def __init__(self, master):
        self.bg_state = 1
        self.fullscreen = False
        self.found_cache = False
        self.reboot_path = os.path.abspath(__file__)
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.folder_dir = os.path.dirname(os.path.abspath(__file__))

        self.root = master
        root.attributes('-fullscreen', True)
        root.after(0, lambda: root.state('zoomed'))
        root.title("HidlowTools-GUI-V2")
        ctk.set_appearance_mode("Dark")
        time1 = datetime.now().strftime("%H:%M:%S")
        data1 = date.today()

        self.cli_files = Subprocess_scripts()
        self.prepare = Prepare_utils(self)
        self.btn2 = None
        self.exit_buttons = None
        self.reboot_buttons = None

        try:
            # загрузка файлов из assets/
            self.exit_buttons = [ctk.CTkImage(light_image=Image.open(f"assets/exit_assets/exitbutton{i}.png").resize((27, 27)),size=(27, 27)) for i in range(1, 3)]
            self.reboot_buttons = [ctk.CTkImage(light_image=Image.open(f"assets/reboot_assets/rebootbutton{i}.png").resize((25, 25)), size=(25, 25)) for i in range(1, 3)]

        except Exception as b:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.LIGHTRED_EX}Error: {b}")

        print(f"{Style.BRIGHT}{Fore.BLUE}GitHub: https://github.com/hiikikomorii {Fore.RESET}|{Fore.LIGHTCYAN_EX} {data1} - {time1}")

        self._widgets()


    def _widgets(self):
        # главное меню
        self.menu_frame = ctk.CTkFrame(self.root, fg_color="#242424")
        self.menu_frame.pack(pady=20)

        # главное меню №2
        self.menu_frame2 = ctk.CTkFrame(self.root, fg_color="#242424")
        self.menu_frame2.pack(pady=15)

        # settigs frame
        self.settings_frame = ctk.CTkFrame(self.root, fg_color="#242424")

        # about frame
        self.about_frame = ctk.CTkFrame(self.root, fg_color="#242424")

        # currency frame
        self.currency_frame = ctk.CTkFrame(self.root, fg_color="#242424")

        # faker frame
        self.faker_frame = ctk.CTkFrame(self.root, fg_color="#242424")

        # monitor frame
        self.monitor_frame = ctk.CTkFrame(self.root, fg_color="#242424")
        self.monitor_frame_stat = ctk.CTkFrame(self.root, fg_color="#242424")

        # кнопки
        self.button1 = ctk.CTkButton(self.menu_frame, text="Number", width=50, corner_radius=10, command= self.prepare.select_api1).pack(side="left", padx=5)
        self.button2 = ctk.CTkButton(self.menu_frame, text="IP", width=50, corner_radius=10, command=self.prepare.select_api2).pack(side="left", padx=5)
        self.button3 = ctk.CTkButton(self.menu_frame, text="Lat/Lon", width=50, corner_radius=10, command=self.prepare.select_api3).pack(side="left", padx=5)
        self.button4 = ctk.CTkButton(self.menu_frame, text="Currency", width=50, corner_radius=10, command=self.prepare.select_currency).pack(side="left", padx=5)
        self.button5 = ctk.CTkButton(self.menu_frame, text="Troll", width=50, corner_radius=10, command=self.cli_files.trol).pack(side="left",padx=5)
        self.button6 = ctk.CTkButton(self.menu_frame, text="API", width=50, corner_radius=10, command=self.cli_files.hidlowapi_cmd).pack(side="left", padx=5)
        self.button7 = ctk.CTkButton(self.menu_frame, text="GPT CHC", width=50, corner_radius=10, command=self.prepare.select_gptchc).pack(side="left", padx=5)
        self.button8 = ctk.CTkButton(self.menu_frame, text="Faker", width=50, corner_radius=10, command=self.prepare.select_faker).pack(side="left", padx=5)
        self.button9 = ctk.CTkButton(self.menu_frame, text="QRcode", width=50, corner_radius=10, command=self.prepare.select_qrcode).pack(side="left", padx=5)
        self.button10 = ctk.CTkButton(self.menu_frame, text="Ctypes Notif", width=50, corner_radius=10, command=self.prepare.select_notify).pack(side="left", padx=5)
        self.button11 = ctk.CTkButton(self.menu_frame, text="Monitoring", width=50, corner_radius=10, command=self.prepare.select_monitor).pack(side="left", padx=5)

        # buttons in menu_frame2
        self.about_btn = ctk.CTkButton(self.menu_frame2, text="Info", text_color="white", width=5, command=lambda: self.prepare.select_about(self.about_frame)).pack(side="left", padx=5)
        self.settings_button = ctk.CTkButton(self.menu_frame2, text="Settings", text_color="white", width=10, corner_radius=10, command=self.toggle_settings).pack(side="left", padx=5)

        # buttons in settings
        self.btn1 = ctk.CTkButton(self.settings_frame, text="Fullscreen", text_color="#00CF00", width=85, corner_radius=10, command=self.toggle_fullscreen)
        self.btn1.pack(pady=2)
        self.btn2 = ctk.CTkButton(self.settings_frame, text="Theme", text_color="white", width=90, corner_radius=10, command=self.change_background).pack(pady=3)
        self.btn3 = ctk.CTkButton(self.settings_frame, text="Clear cache", text_color="white", width=90, corner_radius=10, command=self.clear_cache).pack(pady=3)
        self.btn4 = ctk.CTkButton(self.settings_frame, text="Folder", text_color="white", width=90, corner_radius=10, command=self.open_folder).pack(pady=3)
        self.btn5 = ctk.CTkButton(self.settings_frame, text="Debug", text_color="white", width=90, corner_radius=10, command=self.cli_files.consoleadapter).pack(pady=3)

        # custom buttons exit & reboot
        self.exitadapter_button = ctk.CTkButton(self.menu_frame2, text="", image=self.exit_buttons[0], fg_color="transparent", hover_color="#242424", corner_radius=0, border_width=2,border_color="#242424", width=10, command=Main.exit)
        self.exitadapter_button.pack(side="right", padx=5)
        self.rebootbutton_button = ctk.CTkButton(self.menu_frame2, text="", image=self.reboot_buttons[0], fg_color="transparent", hover_color="#242424", corner_radius=0, border_width=2,border_color="#242424", width=10, command=self.menu_reboot)
        self.rebootbutton_button.pack(side="right", padx=5)

        # ввод
        self.entry_frame = ctk.CTkFrame(self.root, width=200, height=30, fg_color="#242424")
        self.ext_entry_frame = ctk.CTkFrame(self.root, width=200, height=30, fg_color="#242424")
        self.textbox_frame = ctk.CTkFrame(self.root, fg_color="#242424")
        self.entry = ctk.CTkEntry(self.root)
        self.confirm_button = ctk.CTkButton(self.entry_frame, text="OK", text_color="#00CF00", width=50)
        self.confirm_button.pack(side="left", padx=5)
        self.back_button = ctk.CTkButton(self.entry_frame, text="Back", text_color="red", width=50, command=self.go_back_from_entry)
        self.back_button.pack(side="left", padx=5)
        self.paste_btn = ctk.CTkButton(self.ext_entry_frame, text="Paste", width=50, command=self.paste)
        self.paste_btn.pack(side="left", padx=5)
        self.copy_btn = ctk.CTkButton(self.ext_entry_frame, text="Copy", width=50)
        self.copy_btn.pack(side="left", padx=5)

        # back about & info
        self.aboutback_button = ctk.CTkButton(self.about_frame, text="Back", text_color="red", width=10, command=lambda: self.prepare.go_back(self.about_frame))
        self.aboutback_button.pack(pady=5)

        # currency
        self.btc_button = ctk.CTkButton(self.currency_frame, text="BTC", text_color="white", width=5, command=self.prepare.btc_pr).pack(pady=3)
        self.ton_button = ctk.CTkButton(self.currency_frame, text="TON", text_color="white", width=5, command=self.prepare.ton_pr).pack(pady=3)
        self.currencyback_button = ctk.CTkButton(self.currency_frame, text="Back", text_color="red", width=5, command=lambda: self.prepare.go_back(self.currency_frame))
        self.currencyback_button.pack(pady=1)

        # faker
        self.rubtn = ctk.CTkButton(self.faker_frame, text="Russian", text_color="white", width=80, command=self.prepare.faker_ru_pr).pack(pady=3)

        self.engbtn = ctk.CTkButton(self.faker_frame, text="English", text_color="white", width=80, command=self.prepare.faker_eng_pr).pack(pady=3)
        self.kzbtn = ctk.CTkButton(self.faker_frame, text="Spanish", text_color="white", width=80, command=self.prepare.faker_es_pr).pack(pady=3)
        self.jpbtn = ctk.CTkButton(self.faker_frame, text="Japanese", text_color="white", width=80, command=self.prepare.faker_jp_pr).pack(pady=3)
        self.fakerback_button = ctk.CTkButton(self.faker_frame, text="Back", text_color="red", width=80, command=lambda: self.prepare.go_back(self.faker_frame))
        self.fakerback_button.pack(pady=3)

        # monitor
        self.label_mon = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 30))
        self.label_mem = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 30))
        self.label_cpu = ctk.CTkLabel(self.monitor_frame, text_color="white", font=("Arial", 30))
        self.label_info_monitor = ctk.CTkLabel(self.monitor_frame_stat, text_color="white", font=("Arial", 18))
        self.monitorback_button = ctk.CTkButton(self.monitor_frame, text="Back", text_color="red", width=8, command=self.go_back_monitoring)
        self.monitorback_button.pack(side="bottom", pady=1)

        # labels
        self.output_label = ctk.CTkLabel(self.root, text_color="#FF0000")
        self.copyable = ctk.CTkTextbox(self.root)

    # prepare hide main menu
    def prepare_hide(self):
        self.hide_settings()
        self.menu_frame.pack_forget()
        self.menu_frame2.pack_forget()

    def go_back_from_entry(self):
        # выход из entry-фрейма в главное меню
        self.entry.pack_forget()
        self.entry_frame.pack_forget()
        self.ext_entry_frame.pack_forget()
        self.textbox_frame.pack_forget()
        for widget in self.root.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.pack_forget()
        self.menu_frame.pack(pady=20)
        self.menu_frame2.pack(pady=20)

    def go_back_monitoring(self):
        # выход из утилиты monitoring в главное меню
        self.monitor_frame_stat.pack_forget()
        self.label_info_monitor.pack_forget()
        self.monitor_frame.pack_forget()
        self.menu_frame.pack(pady=20)
        self.menu_frame2.pack(pady=20)

    def toggle_settings(self):
        if self.settings_frame.winfo_ismapped():
            self.settings_frame.pack_forget()
        else:
            self.settings_frame.pack(padx=1, pady=1)

    def hide_settings(self):
        if self.settings_frame.winfo_ismapped():
            self.settings_frame.pack_forget()

    def paste(self):
        paste_text = self.root.clipboard_get()
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, paste_text)

    def toggle_fullscreen(self):
        # включает\выключает полноэкранный режим

        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

        if self.fullscreen:
            self.root.attributes("-fullscreen", False)
            self.root.state("normal")
            self.root.geometry("1146x542")
            self.btn1.configure(text_color="#CF0000")
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} RootGeometry '{Fore.MAGENTA}1146x542{Fore.RESET}'")
        else:
            self.root.state('zoomed')
            self.root.attributes("-fullscreen", True)
            self.btn1.configure(text_color="#00CF00")
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} RootGeometry '{Fore.MAGENTA}Fullscreen{Fore.RESET}'")

    def open_folder(self):
        # открывает директорию где находится main.py
        try:
            os.startfile(self.folder_dir)
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Directory '{Fore.MAGENTA}{__file__}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}was opened")
        except Exception as error_folder:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.RED}Произошла ошибка при открытии '{__file__}'\n{error_folder}")

    def clear_cache(self):
        # очистка __pycache__
        import shutil

        for wroot, dirs, files in os.walk(self.root_dir):
            if '__pycache__' in dirs:
                cache_path = os.path.join(wroot, '__pycache__')
                shutil.rmtree(cache_path)
                print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Has been cleared: {Fore.MAGENTA}{cache_path}")
                self.found_cache = True
                return

        if not self.found_cache:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Cache not found")
        else:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Cache not found")

    @staticmethod
    def exit():
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.LIGHTRED_EX}exit")
        sys.exit()

    def menu_reboot(self):
        # перезагрузка скрипта
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} restart GUI..")
        subprocess.Popen(
            ["cmd", "/k", sys.executable, str(self.reboot_path)],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        sys.exit()

    def change_background(self):
        if self.bg_state == 1:
            # white
            self.exitadapter_button.configure(image=self.exit_buttons[1])
            self.rebootbutton_button.configure(image=self.reboot_buttons[1])

            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Apperance mode | {Style.BRIGHT}{Fore.LIGHTWHITE_EX}LIGHT")

            try:
                for frame in (self.menu_frame, self.menu_frame2, self.settings_frame, self.about_frame, self.currency_frame,
                              self.entry_frame, self.faker_frame, self.monitor_frame, self.monitor_frame_stat):
                    frame.configure(fg_color="#EBEBEB")
                self.exitadapter_button.configure(hover_color="#EBEBEB", border_color="#EBEBEB")
                self.rebootbutton_button.configure(hover_color="#EBEBEB", border_color="#EBEBEB")
                self.btn1.configure(text_color="#005E00")

                for labels in (self.monitor_frame_stat, self.monitor_frame):
                    for labels_wid in labels.winfo_children():
                        if isinstance(labels_wid, ctk.CTkLabel):
                            labels_wid.configure(
                                text_color="black"
                            )

                ctk.set_appearance_mode("Light")
            except Exception as a:
                print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.LIGHTRED_EX}error light mode: {a}")

            self.bg_state = 2

        else:
            # black
            self.exitadapter_button.configure(image=self.exit_buttons[0])
            self.rebootbutton_button.configure(image=self.reboot_buttons[0])

            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Apperance mode | {Fore.LIGHTBLACK_EX}BLACK")

            try:
                for frame in (self.menu_frame, self.menu_frame2, self.settings_frame, self.about_frame,
                              self.currency_frame, self.entry_frame, self.faker_frame,self.monitor_frame, self.monitor_frame_stat):
                    frame.configure(fg_color="#242424")

                self.exitadapter_button.configure(hover_color="#242424", border_color="#242424")
                self.rebootbutton_button.configure(hover_color="#242424", border_color="#242424")
                self.btn1.configure(text_color="#00CF00")

                for labels in (self.monitor_frame_stat, self.monitor_frame):
                    for labels_wid in labels.winfo_children():
                        if isinstance(labels_wid, ctk.CTkLabel):
                            labels_wid.configure(
                                text_color="white"
                            )
                ctk.set_appearance_mode("Dark")

            except Exception as a:
                print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.LIGHTRED_EX}Ошибка background: {a}")
            self.bg_state = 1

        try:
            # check fullscreen color
            if self.fullscreen:
                self.btn1.configure(text_color="#CF0000")
            else:
                if self.bg_state == 1:
                    self.btn1.configure(text_color="#00CF00")
                else:
                    self.btn1.configure(text_color="#005E00")
        except Exception as error_fg_fullscreen:
            print(f"{Fore.RED}error check fullscreen color: \n{error_fg_fullscreen}")

    def about_project(self):
        for widget in self.about_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        copyable = ctk.CTkTextbox(
            self.about_frame,
            width=700,
            height=700,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        copyable.pack(padx=20, pady=20)
        print(f"{Fore.BLUE}{Style.BRIGHT}[INFO]{Fore.RESET} {Fore.MAGENTA}About project{Fore.RESET} | {Fore.LIGHTGREEN_EX}was shown")
        text = f"""
        number - показывает информацию о введенном номере\n
        ip - показывает информацию о введенном ip\n
        lat/lon - показывает информаю по введенной долготе(lat) и широте(lon)\n
        qrcode - создает qrcode.png которая содержит вашу ссылку\n
        troll - отдельный скрипт который троллится за вас используя text.txt\n
        currency - выводит курс о BTC и TON в $ & ₽\n
        GPT CHC - Gpt chat history converter вытаскивает .json файл,
        затем переводит его в .txt для чтения\n
        Faker - генерирует фейк данные.\n
        API - маленький API сервер на Flask
        документация: https://github.com/hiikikomorii/API-Server\n
        Window notif - создает windows-уведомление: название окна, значок, текст
        пример: [window] [error] [text in window]
        доступные значки: info, warning, error, question\n
        Monitor - показывает информацию о системе в реальном времени\n
        \n
        background имеет 2 фона: Light и Dark\n
        fullscreen меняет размер окна из полноэкранного режима в 1146x542\n
        debug - консоль отладки показывает информацию о системе и используется
        для проверки на правильную работу утилит\n
        Версия: https://github.com/hiikikomorii/hidlowToolsGUI/blob/main/documentation/CHANGELOG.md\n"""

        copyable.insert("1.0", text)
        copyable.bind("<Key>", lambda s: "break")
        copyable.configure(cursor="arrow")


if __name__ == '__main__':
    root = ctk.CTk()
    app = Main(root)
    root.mainloop()
