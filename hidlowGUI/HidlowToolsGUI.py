import subprocess
import sys
import os
from datetime import date, datetime
from pathlib import Path
import threading
import ctypes

def nomodule_boottraper():
    boot_path = "boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c" , sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()


try:
    import customtkinter as ctk
    from PIL import Image, ImageTk
    from colorama import init, Fore, Style


except ModuleNotFoundError as e:
    nomodule_boottraper()

root = ctk.CTk()
init(autoreset=True)
fullscreen = False
ctk.set_appearance_mode("Dark")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
time1 = datetime.now().strftime("%H:%M:%S")
data1 = date.today()

print(f"{Style.BRIGHT}{Fore.BLUE}GitHub: https://github.com/hiikikomorii {Fore.RESET}|{Fore.LIGHTCYAN_EX} {data1} - {time1}")

# настройка gui
root.attributes('-fullscreen', True)
root.after(0, lambda:root.state('zoomed'))
root.title("HidlowTools-GUI-V2")


# number api util
def select_api1():
    from files.number_api_util import api_number
    clear_entry_frame()
    prepare_input(lambda: api_number(entry, output_label, entry_frame))

# ip api util
def select_api2():
    from files.main_api_utils import api_ip
    clear_entry_frame()
    prepare_input(lambda: api_ip(entry, output_label, entry_frame))

# geo api util
def select_api3():
    from files.main_api_utils import api_lat
    clear_entry_frame()
    prepare_input(lambda: api_lat(entry, output_label, entry_frame))

#prepare spawn currency-frame
def select_currency():
    prepare_hide()
    currency_frame.pack(pady=10)

#prepare util
def ton_pr():
    from files.main_api_utils import select_ton
    select_ton(currency_frame)

#prepare util
def btc_pr():
    from files.main_api_utils import select_btc
    select_btc(currency_frame)

#prepare util
def select_gptchc():
    from files.none_textbox_utils import gpthch, extract_chat
    clear_entry_frame()
    prepare_input(lambda: gpthch(entry, output_label))

# prepare spawn faker-frame
def select_faker():
    prepare_hide()
    faker_frame.pack(pady=10)

def faker_ru_pr():
    from files.faker_func import faker_ru
    for widget in faker_frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()
    faker_ru(faker_frame)

#prepare faker eng
def faker_eng_pr():
    from files.faker_func import faker_eng
    for widget in faker_frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()
    faker_eng(faker_frame)

# prepare faker spain
def faker_es_pr():
    from files.faker_func import faker_es
    for widget in faker_frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()
    faker_es(faker_frame)

#prepare faker japanese
def faker_jp_pr():
    from files.faker_func import faker_jp
    for widget in faker_frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()
    faker_jp(faker_frame)

#prepare util
def select_qrcode():
    from files.none_textbox_utils import qrcodee
    prepare_input(lambda: qrcodee(entry, output_label))

#prepare util
def select_notify():
    from files.none_textbox_utils import ctypes_notify
    prepare_hide()
    prepare_input(lambda: ctypes_notify(entry, output_label))

#prepare monitoring util
def select_monitor():
    from files.monitoring_util import monitoring_start
    prepare_hide()
    monitor_frame.pack(padx=20)
    monitor_frame_stat.pack(side="left", anchor="sw", padx=20)
    threading.Thread(target=lambda: monitoring_start(label_mon, label_mem, label_cpu, label_info_monitor), daemon=True).start()


#prepare entry
def prepare_input(api_func):
    prepare_hide()
    clear_entry_frame()
    entry_frame.pack(pady=10)
    confirm_button.configure(command=api_func)
#prepare hide main menu
def prepare_hide():
    hide_settings()
    menu_frame.pack_forget()
    menu_frame2.pack_forget()



def trol():
    check_path = Path(r"files\troll\trollhidlowGUI.py")

    try:
        if check_path.exists():
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} {Fore.MAGENTA}TrollGidlowGUI{Fore.RESET} | {Fore.LIGHTGREEN_EX}was opened")
            script_dir = Path(__file__).parent / "files" / "troll"
            script_file = script_dir / "trollhidlowGUI.py"

            subprocess.Popen(
                ["cmd", "/c", sys.executable, str(script_file)],
                cwd=str(script_dir),
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            ctypes.windll.user32.MessageBoxW(0, f"Ошибка открытия TrollGUI\nПроверьте совместимость сборки", "HidlowToolsGUI", 0x10)
    except Exception as error_troll_cmd:
        print(error_troll_cmd)

#HidlowAPI
def hidlowapi_cmd():
    check_path = Path(r"files\hidlowAPI.py")

    try:
        if check_path.exists():
            print(f"{Fore.BLUE}{Style.BRIGHT}[API Server]{Fore.RESET} {Fore.MAGENTA}HidlowAPI{Fore.RESET} | {Fore.LIGHTGREEN_EX}was enabled")
            script_dir = Path(__file__).parent / "files"
            script_file = script_dir / "hidlowAPI.py"

            subprocess.Popen(
                ["cmd", "/c", sys.executable, str(script_file)],
                cwd=str(script_dir),
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            ctypes.windll.user32.MessageBoxW(0, f"Ошибка запуска HidlowAPI\nПроверьте совместимость сборки", "HidlowToolsGUI", 0x10)
            print(f"{Fore.BLUE}{Style.BRIGHT}[API Server]{Style.NORMAL} {Fore.LIGHTRED_EX}Error")
    except Exception as error_api_cmd:
        print(error_api_cmd)

#console
def consoleadapter():
    try:
        check_path_debug = Path(r"files\consoledebug\debugconsole.py")
        if check_path_debug.exists():
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.MAGENTA}Debugconsole{Fore.RESET} | {Fore.LIGHTGREEN_EX}was opened")
            script_dir = Path(__file__).parent / "files" / "consoledebug"
            script_file = script_dir / "debugconsole.py"
            subprocess.Popen(
                ["cmd", "/c", sys.executable, str(script_file)],
                cwd=str(script_dir),
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM] {Fore.RED}Debugconsole is not available\n")
            ctypes.windll.user32.MessageBoxW(0, f"Сборка повреждена\nКонсоль недоступна\nПроверьте совместимость сборки", "debug-console", 0x10)
    except Exception as error_prepare_console:
        print(error_prepare_console)


#prepare about
def select_about():
    prepare_hide()
    about_frame.pack(pady=10)
    about_project()
    aboutback_button.configure(command=lambda: go_back(about_frame))

# о проекте
def about_project():
    for widget in about_frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()

    copyable = ctk.CTkTextbox(
        about_frame,
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


# эти 2 блока с припиской _settings показывают\скрывают настройки
def toggle_settings():
    if settings_frame.winfo_ismapped():
        settings_frame.pack_forget()
    else:
        settings_frame.pack(padx=1, pady=1)

def hide_settings():
    if settings_frame.winfo_ismapped():
        settings_frame.pack_forget()

def toggle_fullscreen():
    # включает\выключает полноэкранный режим
    global fullscreen
    global bg_state
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

    if fullscreen:
        root.attributes("-fullscreen", False)
        root.state("normal")
        root.geometry("1146x542")
        btn1.configure(text_color="#CF0000")
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} RootGeometry '{Fore.MAGENTA}1146x542{Fore.RESET}'")
    else:
        root.state('zoomed')
        root.attributes("-fullscreen", True)
        btn1.configure(text_color="#00CF00")
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} RootGeometry '{Fore.MAGENTA}Fullscreen{Fore.RESET}'")

def open_folder():
    # открывает директорию где находится HidlowToolsGUI.py
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        os.startfile(current_dir)
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Directory '{Fore.MAGENTA}{__file__}{Fore.RESET}' | {Fore.LIGHTGREEN_EX}was opened")

    except Exception as error_folder:
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.RED}Произошла ошибка при открытии '{__file__}'\n{error_folder}")

def clear_cache():
    # очистка pycache
    import shutil
    root_dir = os.path.dirname(os.path.abspath(__file__))
    found_cache = False

    for wroot, dirs, files in os.walk(root_dir):
        if '__pycache__' in dirs:
            cache_path = os.path.join(wroot, '__pycache__')
            shutil.rmtree(cache_path)
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Has been cleared: {Fore.MAGENTA}{cache_path}")
            found_cache = True
    if not found_cache:
        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Cache not found")

def exitt():
    # выход
    print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.LIGHTRED_EX}exiting{Fore.RESET} the program")
    sys.exit()


def menu_reboot():
    # перезагрузка скрипта
    print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} restart GUI..")
    script_path = os.path.abspath(__file__)
    subprocess.Popen(
        ["cmd", "/k", sys.executable, str(script_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()



def go_back_from_entry():
    # выход из entry-фрейма в главное меню
    entry_frame.pack_forget()
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkLabel):
            widget.pack_forget()
    menu_frame.pack(pady=20)
    menu_frame2.pack(pady=20)

def go_back_monitoring():
    # выход из утилиты monitoring в главное меню
    monitor_frame_stat.pack_forget()
    label_info_monitor.pack_forget()
    monitor_frame.pack_forget()
    menu_frame.pack(pady=20)
    menu_frame2.pack(pady=20)

def go_back(hide_frame):
    # основная функция выхода в главное меню
    hide_frame.pack_forget()
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkLabel):
            widget.pack_forget()
    menu_frame.pack(pady=20)
    menu_frame2.pack(pady=20)

def clear_entry_frame():
    # очиста ввода
    entry.delete(0, "end")
    for widget in entry_frame.winfo_children():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()



btn2 = None
exit_buttons = None
reboot_buttons = None

try:
    # загрузка файлов из assets/
    exit_buttons = [ctk.CTkImage(light_image=Image.open(f"assets/exit_assets/exitbutton{i}.png").resize((27, 27)), size=(27, 27))for i in range(1, 3)]
    reboot_buttons = [ctk.CTkImage(light_image=Image.open(f"assets/reboot_assets/rebootbutton{i}.png").resize((25, 25)), size=(25, 25)) for i in range(1, 3)]

except Exception as b:
    print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} {Fore.LIGHTRED_EX}Error: {b}")

bg_state = 1

def change_background():
    global bg_state
    global fullscreen

    if bg_state == 1:
        # white
        exitadapter_button.configure(image=exit_buttons[1])
        rebootbutton_button.configure(image=reboot_buttons[1])

        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Apperance mode | {Style.BRIGHT}{Fore.LIGHTWHITE_EX}LIGHT")

        try:
            for frame in (menu_frame, menu_frame2, settings_frame, about_frame, currency_frame, entry_frame, faker_frame, monitor_frame, monitor_frame_stat):
                frame.configure(fg_color="#EBEBEB")
            exitadapter_button.configure(hover_color="#EBEBEB", border_color="#EBEBEB")
            rebootbutton_button.configure(hover_color="#EBEBEB", border_color="#EBEBEB")
            btn1.configure(text_color="#005E00")

            for labels in (monitor_frame_stat, monitor_frame):
                for labels_wid in labels.winfo_children():
                    if isinstance(labels_wid, ctk.CTkLabel):
                        labels_wid.configure(
                            text_color="black"
                        )

            ctk.set_appearance_mode("Light")
        except Exception as a:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.LIGHTRED_EX}error light mode: {a}")

        bg_state = 2

    else:
        # black
        exitadapter_button.configure(image=exit_buttons[0])
        rebootbutton_button.configure(image=reboot_buttons[0])

        print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.RESET} Apperance mode | {Fore.LIGHTBLACK_EX}BLACK")

        try:
            for frame in (menu_frame, menu_frame2, settings_frame, about_frame, currency_frame, entry_frame, faker_frame, monitor_frame, monitor_frame_stat):
                frame.configure(fg_color="#242424")

            exitadapter_button.configure(hover_color="#242424", border_color="#242424")
            rebootbutton_button.configure(hover_color="#242424", border_color="#242424")
            btn1.configure(text_color="#00CF00")

            for labels in (monitor_frame_stat, monitor_frame):
                for labels_wid in labels.winfo_children():
                    if isinstance(labels_wid, ctk.CTkLabel):
                        labels_wid.configure(
                            text_color="white"
                        )
            ctk.set_appearance_mode("Dark")

        except Exception as a:
            print(f"{Fore.BLUE}{Style.BRIGHT}[SYSTEM]{Fore.LIGHTRED_EX}Ошибка background: {a}")
        bg_state = 1

    try:
        # check fullscreen color
        if fullscreen:
            btn1.configure(text_color="#CF0000")
        else:
            if bg_state == 1:
                btn1.configure(text_color="#00CF00")
            else:
                btn1.configure(text_color="#005E00")
    except Exception as error_fg_fullscreen:
        print(f"{Fore.RED}error check fullscreen color: \n{error_fg_fullscreen}")


# главное меню
menu_frame = ctk.CTkFrame(root, fg_color="#242424")
menu_frame.pack(pady=20)

# главное меню №2
menu_frame2 = ctk.CTkFrame(root, fg_color="#242424")
menu_frame2.pack(pady=15)

# settigs frame
settings_frame = ctk.CTkFrame(root, fg_color="#242424")

# about frame
about_frame = ctk.CTkFrame(root, fg_color="#242424")

# currency frame
currency_frame = ctk.CTkFrame(root, fg_color="#242424")

#faker frame
faker_frame = ctk.CTkFrame(root, fg_color="#242424")

#monitor frame
monitor_frame = ctk.CTkFrame(root, fg_color="#242424")
monitor_frame_stat = ctk.CTkFrame(root, fg_color="#242424")

# кнопки
button1 = ctk.CTkButton(menu_frame, text="Number", width=50, corner_radius=10, command=select_api1).pack(side="left", padx=5)
button2 = ctk.CTkButton(menu_frame, text="IP", width=50, corner_radius=10, command=select_api2).pack(side="left", padx=5)
button3 = ctk.CTkButton(menu_frame, text="Lat/Lon", width=50, corner_radius=10, command=select_api3).pack(side="left", padx=5)
button4 = ctk.CTkButton(menu_frame, text="Currency", width=50, corner_radius=10, command=select_currency).pack(side="left", padx=5)
button5 = ctk.CTkButton(menu_frame, text="Troll", width=50, corner_radius=10, command=trol).pack(side="left", padx=5)
button6 = ctk.CTkButton(menu_frame, text="API", width=50, corner_radius=10, command=hidlowapi_cmd).pack(side="left", padx=5)
button7 = ctk.CTkButton(menu_frame, text="GPT CHC", width=50, corner_radius=10, command=select_gptchc).pack(side="left", padx=5)
button8 = ctk.CTkButton(menu_frame, text="Faker", width=50, corner_radius=10, command=select_faker).pack(side="left", padx=5)
button9 = ctk.CTkButton(menu_frame, text="QRcode", width=50, corner_radius=10, command=select_qrcode).pack(side="left", padx=5)
button10 = ctk.CTkButton(menu_frame, text="Ctypes Notif",width=50, corner_radius=10, command=select_notify).pack(side="left", padx=5)
button11 = ctk.CTkButton(menu_frame, text="Monitoring", width=50, corner_radius=10, command=select_monitor).pack(side="left", padx=5)

#buttons in menu_frame2
about_btn = ctk.CTkButton(menu_frame2, text="Info", text_color="white", width=5, command=select_about).pack(side="left", padx=5)
settings_button = ctk.CTkButton(menu_frame2, text="Settings", text_color="white", width=10, corner_radius=10, command=toggle_settings).pack(side="left", padx=5)

#buttons in settings
btn1 = ctk.CTkButton(settings_frame, text="Fullscreen", text_color="#00CF00", width=85, corner_radius=10, command=toggle_fullscreen)
btn1.pack(pady=2)
btn2 = ctk.CTkButton(settings_frame, text="Theme", text_color="white", width=90, corner_radius=10, command=change_background).pack(pady=3)
btn3 = ctk.CTkButton(settings_frame, text="Clear cache", text_color="white", width=90, corner_radius=10, command=clear_cache).pack(pady=3)
btn4 = ctk.CTkButton(settings_frame, text="Folder", text_color="white", width=90, corner_radius=10, command=open_folder).pack(pady=3)
btn5 = ctk.CTkButton(settings_frame, text="Debug", text_color="white", width=90, corner_radius=10, command=consoleadapter).pack(pady=3)


#custom buttons exit & reboot
exitadapter_button = ctk.CTkButton(menu_frame2, text="", image=exit_buttons[0], fg_color="transparent", hover_color="#242424", corner_radius=0, border_width=2, border_color="#242424", width=10, command=exitt)
exitadapter_button.pack(side="right", padx=5)
rebootbutton_button = ctk.CTkButton(menu_frame2, text="", image=reboot_buttons[0], fg_color="transparent", hover_color="#242424", corner_radius=0, border_width=2, border_color="#242424", width=10, command=menu_reboot)
rebootbutton_button.pack(side="right", padx=5)

# ввод
entry_frame = ctk.CTkFrame(root, width=200, height=30, fg_color="#242424")
entry = ctk.CTkEntry(entry_frame)
entry.pack(pady=5)
confirm_button = ctk.CTkButton(entry_frame, text="OK", text_color="#00CF00", width=50)
confirm_button.pack(pady=5)
back_button = ctk.CTkButton(entry_frame, text="Back", text_color="red", width=50, command=go_back_from_entry)
back_button.pack(pady=1)

#back about & info
aboutback_button = ctk.CTkButton(about_frame, text="Back", text_color="red", width=10, command=lambda: go_back(about_frame))
aboutback_button.pack(pady=5)

#currency
btc_button = ctk.CTkButton(currency_frame, text="BTC", text_color="white", width=5, command=btc_pr).pack(pady=3)
ton_button = ctk.CTkButton(currency_frame, text="TON", text_color="white", width=5, command=ton_pr).pack(pady=3)
currencyback_button = ctk.CTkButton(currency_frame, text="Back", text_color="red", width=5, command=lambda: go_back(currency_frame))
currencyback_button.pack(pady=1)

#faker
rubtn = ctk.CTkButton(faker_frame, text="Russian", text_color="white", width=80, command=faker_ru_pr).pack(pady=3)
engbtn = ctk.CTkButton(faker_frame, text="English", text_color="white", width=80, command=faker_eng_pr).pack(pady=3)
kzbtn = ctk.CTkButton(faker_frame, text="Spanish", text_color="white", width=80, command=faker_es_pr).pack(pady=3)
jpbtn = ctk.CTkButton(faker_frame, text="Japanese", text_color="white", width=80, command=faker_jp_pr).pack(pady=3)
fakerback_button = ctk.CTkButton(faker_frame, text="Back", text_color="red", width=80, command=lambda: go_back(faker_frame))
fakerback_button.pack(pady=3)


#monitor
label_mon = ctk.CTkLabel(monitor_frame, text_color="white", font=("Arial", 30))
label_mem = ctk.CTkLabel(monitor_frame, text_color="white", font=("Arial", 30))
label_cpu = ctk.CTkLabel(monitor_frame, text_color="white", font=("Arial", 30))
label_info_monitor = ctk.CTkLabel(monitor_frame_stat, text_color="white", font=("Arial", 18))
monitorback_button = ctk.CTkButton(monitor_frame, text="Back", text_color="red", width=8, command=go_back_monitoring)
monitorback_button.pack(side="bottom", pady=1)

#labels
output_label = ctk.CTkLabel(root, text_color="#FF0000")

root.mainloop()
