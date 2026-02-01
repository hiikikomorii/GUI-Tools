def nomodule_boottraper():
    import subprocess
    import sys
    boot_path = "bootstrapper.py"
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
class Utils:
    def __init__(self, label_widget):
        self.label_widget = label_widget

    def qrcodee(self, entry_widget, label_widget):
        try:
            import qrcode
        except ModuleNotFoundError:
            nomodule_boottraper()

        user_input = entry_widget.get().strip()
        label_widget.pack_forget()

        if not user_input:
            self.label_widget.configure(text="Введите URL", text_color="red")
            self.label_widget.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} QRCODE: {Fore.LIGHTYELLOW_EX}URL was not entered")
            return

        try:
            img = qrcode.make(user_input)
            img.save("qrcode.png")
            self.label_widget.configure(text="QRcode сохранен", text_color="green")
            self.label_widget.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} QRCODE: QRcode has been {Fore.LIGHTGREEN_EX}generated{Fore.RESET} and {Fore.LIGHTGREEN_EX}saved{Fore.RESET} as '{Fore.MAGENTA}qrcode.png{Fore.RESET}'")

        except Exception as er:
            self.label_widget.configure(text="error. see log", text_color="red")
            self.label_widget.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} QRCODE: {Fore.LIGHTRED_EX}error: {er}")

    @staticmethod
    def extract_chat(input_path, chat_name, output_path, label_widget):
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
                    "user": "User: ",
                    "assistant": "ChatGPT: ",
                    "system": "[СИСТЕМА]: "
                }.get(author, "")
                messages.append(prefix + text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(messages))

        print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: Chat {Fore.LIGHTMAGENTA_EX}{chat_name}{Fore.RESET} {Fore.LIGHTGREEN_EX}saved{Fore.RESET} as {Style.NORMAL}{Fore.MAGENTA}{output_path}")
        label_widget.configure(text=f"Чат '{chat_name}' сохранён как {output_path}", text_color="#00CF00")
        label_widget.pack(pady=5)

    def gpthch(self, entry_widget, label_widget):

        user_input = entry_widget.get().strip()

        if not user_input:
            self.label_widget.configure(text="Введите имя файла", text_color="red")
            self.label_widget.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: {Fore.LIGHTYELLOW_EX}chat name was not entered")
            return

        try:
            input_file = "conversations.json"
            chat_input_name = user_input
            output_file = "chat_export.txt"

            Utils.extract_chat(input_file, chat_input_name, output_file, label_widget)

        except Exception as er:
            self.label_widget.configure(text="error. see log", text_color="red")
            self.label_widget.pack()
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} GPTCHC: {Fore.LIGHTRED_EX}error: {er}")

    @staticmethod
    def show_messagebox(text, title, icon):
        ctypes.windll.user32.MessageBoxW(0, text, title, icon)

    def ctypes_notify(self, entry_widget, label_widget):
        label_widget.pack_forget()
        import threading
        notify_icons = {
            "info": 0x40,
            "warning": 0x30,
            "error": 0x10,
            "question": 0x20
        }

        parts = entry_widget.get().split(maxsplit=2)

        if not parts:
            self.label_widget.configure(text_color="red", text="title, icon_type, text")
            self.label_widget.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.YELLOW}No data has been entered")
            return
        if len(parts) != 3:
            self.label_widget.configure(text_color="red", text="title, icon_type, text")
            self.label_widget.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.YELLOW}Less than 3 data were entered")
            return

        try:
            title = parts[0]
            icon_type = parts[1].lower()
            text = parts[2]

            icon_code = notify_icons.get(icon_type, 0x10)

            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.MAGENTA}Notification{Fore.RESET} | {Fore.LIGHTGREEN_EX}was shown")
            self.label_widget.configure(text="Notification was shown", text_color="#00CF00")
            self.label_widget.pack(pady=5)

            threading.Thread(target=Utils.show_messagebox, args=(text, title, icon_code), daemon=True).start()

        except Exception as error_ctypes:
            self.label_widget.configure(text=f"error\n{error_ctypes}", text_color="red")
            self.label_widget.pack()
            print(f"{Fore.BLUE}{Style.BRIGHT}[UTILS]{Fore.RESET} CTYPES: {Fore.RED}error: \n{error_ctypes}")

class Example_main:
    def __init__(self, master):
        self.root = master
        self._widgets()
        self.test_utils = Utils(self.label)

    def _widgets(self):
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(pady=5)

        self.entry_frame = ctk.CTkFrame(self.root, width=200, height=30, fg_color="#242424")

        self.entry = ctk.CTkEntry(self.entry_frame)
        self.entry.pack(pady=5)

        self.confirm_button = ctk.CTkButton(self.entry_frame, text="OK", text_color="#00CF00", width=80)
        self.confirm_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self.entry_frame, text="Back", text_color="red", width=80, command=self.go_back_from_entry)
        self.back_button.pack()

        self.label = ctk.CTkLabel(self.root, fg_color="#242424")

        text_gpt_example = "Поместите conversations.json из экспорта истории ChatGPT в папку /files/\nзатем в скрипте напишите точное название чата"
        self.label_gpt_example = ctk.CTkLabel(self.root, text=text_gpt_example, fg_color="#242424")

        self.button_qr = ctk.CTkButton(self.main_frame, text="qrcode", width=80, command=self.prepare_qrcode)
        self.button_qr.pack(side="left", padx=5)

        self.button_notify = ctk.CTkButton(self.main_frame, text="GPTCHC", width=80, command=self.prepare_gptchc)
        self.button_notify.pack(side="left", padx=5)

        self.button_gpt = ctk.CTkButton(self.main_frame, text="Notify", width=80, command=self.prepare_notify)
        self.button_gpt.pack(side="left", padx=5)

        self.example_qrcode_btn = ctk.CTkButton(self.entry_frame, text="example", width=80, command=lambda: self.entry.insert(0, "https://example.com"))
        self.example_notify_btn = ctk.CTkButton(self.entry_frame, text="example", width=80, command=lambda: self.entry.insert(0, "title error text"))

    def go_back_from_entry(self):
        self.example_qrcode_btn.pack_forget()
        self.example_notify_btn.pack_forget()
        self.label.pack_forget()
        self.label_gpt_example.pack_forget()
        self.entry_frame.pack_forget()
        self.main_frame.pack()

    def prepare_input(self, api_func):
        self.entry.delete(0, "end")
        self.main_frame.pack_forget()
        self.entry_frame.pack(pady=10)
        self.confirm_button.configure(command=api_func)


    def prepare_qrcode(self):
        self.prepare_input(lambda: self.test_utils.qrcodee(self.entry, self.label))
        self.example_notify_btn.pack_forget()
        self.example_qrcode_btn.pack(pady=5)

    def prepare_gptchc(self):
        self.prepare_input(lambda: self.test_utils.gpthch(self.entry, self.label))
        self.example_notify_btn.pack_forget()
        self.example_qrcode_btn.pack_forget()
        self.back_button.pack()
        self.label_gpt_example.pack(pady=5)


    def prepare_notify(self):
        self.prepare_input(lambda: self.test_utils.ctypes_notify(self.entry, self.label))
        self.example_qrcode_btn.pack_forget()
        self.example_notify_btn.pack(pady=5)

if __name__ == '__main__':
    root = ctk.CTk()
    app = Example_main(root)
    root.mainloop()