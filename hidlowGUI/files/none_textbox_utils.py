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
    import customtkinter as ctk
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
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} QRCODE: {Fore.LIGHTYELLOW_EX}URL was not entered")
        return

    try:
        img = qrcode.make(user_input)
        img.save("qrcode.png")
        label_widget.configure(text="QRcode сохранен", text_color="green")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} QRCODE: QRcode has been {Fore.LIGHTGREEN_EX}generated{Fore.RESET} and {Fore.LIGHTGREEN_EX}saved{Fore.RESET} as '{Fore.MAGENTA}qrcode.png{Fore.RESET}'")

    except Exception as er:

        label_widget.configure(text="error. see log", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} QRCODE: {Fore.LIGHTRED_EX}error: {er}")




def extract_chat(input_path, chat_name, output_path, label_widget=None):
    import json
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chat = next((conv for conv in data if conv.get("title") == chat_name), None)
    if not chat:
        label_widget.configure(text=f"чат с названием '{chat_name}' не найден", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: chat with the name '{Fore.MAGENTA}{chat_name}{Fore.RESET}' {Fore.LIGHTRED_EX}not found")
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

    print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: Chat {Fore.LIGHTMAGENTA_EX}{chat_name}{Fore.RESET} {Fore.LIGHTGREEN_EX}saved{Fore.RESET} as {Style.NORMAL}{Fore.MAGENTA}{output_path}")
    label_widget.configure(text=f"Чат '{chat_name}' сохранён как {output_path}", text_color="#00CF00")
    label_widget.pack(pady=5)

def gpthch(entry_widget, label_widget):

    user_input = entry_widget.get().strip()


    if not user_input:
        label_widget.configure(text="Введите имя файла", text_color="red")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: {Fore.LIGHTYELLOW_EX}chat name was not entered")
        return

    try:
        input_file = "conversations.json"
        chat_input_name = user_input
        output_file = "chat_export.txt"

        extract_chat(input_file, chat_input_name, output_file, label_widget)

    except Exception as er:
        label_widget.configure(text="error. see log", text_color="red")
        label_widget.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: {Fore.LIGHTRED_EX}error: {er}")

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
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.YELLOW}No data has been entered")
        return
    if len(parts) != 3:
        label_widget.configure(text_color="red", text="title, icon_type, text")
        label_widget.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.YELLOW}Less than 3 data were entered")
        return

    try:
        title = parts[0]
        icon_type = parts[1].lower()
        text = parts[2]

        icon_code = notify_icons.get(icon_type, 0x10)

        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.MAGENTA}Notification{Fore.RESET} | {Fore.LIGHTGREEN_EX}was shown")
        label_widget.configure(text="Notification was shown", text_color="#00CF00")
        label_widget.pack(pady=5)

        threading.Thread(target=show_messagebox, args=(text, title, icon_code), daemon=True).start()

    except Exception as error_ctypes:
        label_widget.configure(text=f"error\n{error_ctypes}", text_color="red")
        label_widget.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.RED}error: \n{error_ctypes}")


def example_test():
    root = ctk.CTk()

    main_frame = ctk.CTkFrame(root)
    main_frame.pack(pady=5)

    def prepare_input(api_func):
        entry.delete(0, "end")
        for widget in entry_frame.winfo_children():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        main_frame.pack_forget()
        entry_frame.pack(pady=10)
        confirm_button.configure(command=api_func)


    def prepare_qrcode():
        prepare_input(lambda: qrcodee(entry, label))
        example_notify_btn.pack_forget()
        example_qrcode_btn.pack(pady=5)

    def prepare_gptchc():
        prepare_input(lambda: gpthch(entry, label))
        example_notify_btn.pack_forget()
        example_qrcode_btn.pack_forget()
        back_button.pack()
        label_gpt_example.pack(pady=5)


    def prepare_notify():
        prepare_input(lambda: ctypes_notify(entry, label))
        example_qrcode_btn.pack_forget()
        example_notify_btn.pack(pady=5)

    def go_back_from_entry():
        example_qrcode_btn.pack_forget()
        example_notify_btn.pack_forget()
        label.destroy()
        label_gpt_example.pack_forget()
        entry_frame.pack_forget()
        main_frame.pack()

    entry_frame = ctk.CTkFrame(root, width=200, height=30, fg_color="#242424")
    entry = ctk.CTkEntry(entry_frame)
    entry.pack(pady=5)
    confirm_button = ctk.CTkButton(entry_frame, text="OK", text_color="#00CF00", width=80)
    confirm_button.pack(pady=5)
    back_button = ctk.CTkButton(entry_frame, text="Back", text_color="red", width=80, command=go_back_from_entry)
    back_button.pack()

    label = ctk.CTkLabel(root, fg_color="#242424")
    text_gpt_example = "Поместите conversations.json из экспорта истории ChatGPT в папку /files/\nзатем в скрипте напишите точное название чата"
    label_gpt_example = ctk.CTkLabel(root, text=text_gpt_example, fg_color="#242424")
    button_qr = ctk.CTkButton(main_frame, text="qrcode", width=80, command=prepare_qrcode)
    button_qr.pack(side="left", padx=5)

    button_notify = ctk.CTkButton(main_frame, text="GPTCHC", width=80, command=prepare_gptchc)
    button_notify.pack(side="left", padx=5)

    button_gpt = ctk.CTkButton(main_frame, text="Notify", width=80, command=prepare_notify)
    button_gpt.pack(side="left", padx=5)

    example_qrcode_btn = ctk.CTkButton(entry_frame, text="example", width=80, command=lambda: entry.insert(0, "https://example.com"))
    example_notify_btn = ctk.CTkButton(entry_frame, text="example", width=80, command=lambda: entry.insert(0, "title error text"))
    root.mainloop()

if __name__ == '__main__':
    example_test()