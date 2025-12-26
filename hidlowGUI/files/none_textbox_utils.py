def nomodule_boottraper():
    import subprocess
    import sys
    boot_path = "../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c" , sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()


try:
    from colorama import init, Fore, Style
    import ctypes
except ModuleNotFoundError:
    nomodule_boottraper()

init(autoreset=True)



#qrcode, gpthch, ctypes notif
def qrcodee(entry_widget, label_widget):
    try:
        import qrcode
    except ModuleNotFoundError:
        nomodule_boottraper()

    user_input = entry_widget.get().strip()
    label_widget.pack_forget()

    if not user_input:
        label_widget.configure(text="Введите URL", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[QR]{Style.NORMAL} {Fore.LIGHTYELLOW_EX}Url не был введен.")
        return

    try:
        img = qrcode.make(user_input)
        img.save("qrcode.png")
        label_widget.configure(text="QRcode сохранен", text_color="green")
        label_widget.pack(pady=5)
        print(
            f"{Fore.BLUE}{Style.BRIGHT}[QR]{Style.NORMAL} {Fore.LIGHTGREEN_EX}QR код сгенерирован и сохранён как 'qrcodde.png'")

    except Exception as er:

        label_widget.configure(text="error. see log", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[QR]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка функции qr: {er}")




def extract_chat(input_path, chat_name, output_path, label_widget=None):
    import json
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chat = next((conv for conv in data if conv.get("title") == chat_name), None)
    if not chat:
        label_widget.configure(text=f"чат с названием '{chat_name}' не найден", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[GPTCHC]{Style.NORMAL} {Fore.RED}Чат с названием '{Style.BRIGHT}{chat_name}{Style.NORMAL}' не найден.")
        return

    messages = []
    for msg in chat.get("mapping", {}).values():
        message = msg.get("message")
        if not message:
            continue

        author = message.get("author", {}).get("role", "unknown")
        content_parts = message.get("content", {}).get("parts", [])
        text_parts = [
            part if isinstance(part, str) else str(part.get("text", part))
            for part in content_parts
        ]
        text = "\n".join(text_parts).strip()

        if text:
            prefix = {
                "user": "Вы: ",
                "assistant": "ChatGPT: ",
                "system": "[СИСТЕМА]: "
            }.get(author, "")
            messages.append(prefix + text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(messages))

    print(f"{Fore.BLUE}{Style.BRIGHT}[GPTCHC]{Style.NORMAL} {Fore.LIGHTGREEN_EX}Чат '{Style.BRIGHT}{chat_name}{Style.NORMAL}' сохранён как {Style.BRIGHT}{output_path}{Style.NORMAL}'")
    label_widget.configure(text=f"Чат '{chat_name}' сохранён как {output_path}", text_color="#00CF00")
    label_widget.pack(pady=5)

def gpthch(entry_widget, label_widget):

    user_input = entry_widget.get().strip()


    if not user_input:
        label_widget.configure(text="Введите имя файла", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[GPTCHC]{Style.NORMAL} {Fore.LIGHTYELLOW_EX}название файла не было введено.")
        return

    try:
        input_file = "conversations.json"
        chat_input_name = user_input
        output_file = "chat_export.txt"

        extract_chat(input_file, chat_input_name, output_file, label_widget)

    except Exception as er:
        label_widget.configure(text="error. see log", text_color="red")
        label_widget.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[GPTCHC]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка функции GPTCHC: {er}")

def show_messagebox(text, title, icon):
    ctypes.windll.user32.MessageBoxW(0, text, title, icon)
def ctypes_notify(entry_widget, label_widget):
    import threading
    notify_icons = {
        "info": 0x40,
        "warning": 0x30,
        "error": 0x10,
        "question": 0x20
    }

    parts = entry_widget.get().split(maxsplit=2)

    if not parts:
        label_widget.configure(text_color="red", text="title, icon_type, text")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[CTYPES]{Style.NORMAL} {Fore.YELLOW}No data has been entered")
        return
    if len(parts) != 3:
        label_widget.configure(text_color="red", text="title, icon_type, text")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[CTYPES]{Style.NORMAL} {Fore.YELLOW}Less than 3 data were entered")
        return

    try:
        title = parts[0]
        icon_type = parts[1].lower()
        text = parts[2]

        icon_code = notify_icons.get(icon_type, 0x10)

        print(f"{Fore.BLUE}{Style.BRIGHT}[CTYPES]{Style.NORMAL} {Fore.GREEN}Notification was shown")
        label_widget.configure(text="Notification was shown", text_color="#00CF00")
        label_widget.pack(pady=5)

        threading.Thread(target=show_messagebox, args=(text, title, icon_code), daemon=True).start()

    except Exception as error_ctypes:
        label_widget.configure(text=f"error\n{error_ctypes}", text_color="red")
        label_widget.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[CTYPES]{Style.NORMAL} {Fore.RED}error ctype\n{error_ctypes}")