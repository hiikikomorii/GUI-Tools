import subprocess
import sys
import ctypes
import tkinter as tk
import threading
try:
    from pynput.keyboard import Controller, Key
    import time
    from colorama import init, Fore

except ModuleNotFoundError as e:
    boot_path = "../../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

init(autoreset=True)
keyboard = Controller()

root = tk.Tk()
root.config(bg="#080808")
label_main = tk.Label(root, bg="#080808", fg="white")


def troll_start():
    try:
        with open("text.txt", "r", encoding="utf-8") as f:
            words = f.read().splitlines()
    except Exception as error_txt:
        ctypes.windll.user32.MessageBoxW(0, f"Сборка повреждена\ntxt не найден\n{error_txt}\nПроверьте совместимость сборки", "troll", 0x10)
        sys.exit()

    i = 0
    label_main.config(text="wait 5 sec..", fg="white")
    label_main.pack()
    time.sleep(5)
    while True:
        while i < len(words):

            for _ in range(10):
                if i >= len(words):
                    print(f"{Fore.LIGHTRED_EX}Скрипт закончен")
                    break

                keyboard.type(words[i])
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(0.5)
                i += 1


def troll_start_thread():
    threading.Thread(target=troll_start, daemon=True).start()

def troll_stop():
    root.destroy()

main_frame = tk.Frame(root, bg="#080808")
main_frame.pack()
main_button = tk.Button(main_frame, text="start", command=troll_start_thread, bg="#080808", fg="white", activebackground="black", activeforeground="white").pack(side="left", padx=10)
stop_button = tk.Button(main_frame, text="exit", command=troll_stop, bg="red", activebackground="red", fg="white").pack(side="left")
root.mainloop()
