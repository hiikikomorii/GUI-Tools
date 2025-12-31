import ctypes
import threading
try:
    import customtkinter as ctk
    from pynput.keyboard import Controller, Key
    import time

except ModuleNotFoundError as e:
    import subprocess
    import sys
    boot_path = "../../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

keyboard = Controller()
stop_event = threading.Event()
thread_instance = None
words = None

root = ctk.CTk()

def troll_start():
    time.sleep(5)
    i = 0

    while i < len(words) and not stop_event.is_set():
        for _ in range(10):
            if stop_event.is_set():
                break
            if i >= len(words):
                print("Скрипт закончен")
                break

            keyboard.type(words[i])
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            i += 1
            time.sleep(0.5)


def troll_start_thread():
    global words
    global thread_instance
    if switch_var.get():
        stop_event.clear()
        try:
            with open("text.txt", "r", encoding="utf-8") as f:
                words = f.read().splitlines()
        except Exception as error_txt:
            ctypes.windll.user32.MessageBoxW(0, f"Сборка повреждена\ntxt не найден\n{error_txt}\nПроверьте совместимость сборки", "troll", 0x10)
            sys.exit()

        thread_instance = threading.Thread(target=troll_start, daemon=True)
        thread_instance.start()
    else:
        stop_event.set()


def troll_stop():
    root.destroy()



main_frame = ctk.CTkFrame(root)
main_frame.pack()

label_main = ctk.CTkLabel(root, text="скрипт начнет работать\nспустя 5 секунд после запуска").pack()

switch_var = ctk.StringVar(value="off")
main_button = ctk.CTkSwitch(main_frame, text="start", command=troll_start_thread, variable=switch_var, onvalue="on", offvalue="off").pack(side="left", padx=10)
stop_button = ctk.CTkButton(main_frame, text="exit", command=troll_stop).pack(side="left")

root.mainloop()
