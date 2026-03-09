try:
    from colorama import init, Fore, Style
    import customtkinter as ctk
    import ctypes
except ModuleNotFoundError:
    pass

def msgb(text, title):
    threading.Thread(target=lambda: ctypes.windll.user32.MessageBoxW(0, text, title, 0x10), daemon=True).start()

class Utils:
    def __init__(self, label_widget):
        self.label_widget = label_widget

    def qrcodee(self, entry_widget, label_widget):
        import qrcode

        user_input = entry_widget.get().strip()
        label_widget.pack_forget()

        if not user_input:
            self.label_widget.configure(text="Введите URL", text_color="red")
            self.label_widget.place(x=359, y=150)
            return

        try:
            img = qrcode.make(user_input)
            img.save("qrcode.png")
            self.label_widget.configure(text="QRcode сохранен", text_color="#00CF00")
            self.label_widget.place(x=344, y=150)

        except Exception as er:
            self.label_widget.configure(text="error", text_color="red")
            self.label_widget.place(x=383, y=150)
            msgb(f"{er}", "qrcode-error")

    @staticmethod
    def extract_chat(input_path, chat_name, output_path, label_widget, extra_widget):
        import json
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        label_widget.place_forget()
        chat = next((conv for conv in data if conv.get("title") == chat_name), None)
        if not chat:
            extra_widget.configure(text=f"чат с названием '{chat_name}' не найден", text_color="red")
            extra_widget.pack(side="bottom", pady=15)
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

        extra_widget.configure(text=f"Чат '{chat_name}' сохранён как {output_path}", text_color="#00CF00")
        extra_widget.pack(side="bottom", pady=15)

    def gpthch(self, entry_widget, label_widget, extra_label):

        user_input = entry_widget.get().strip()

        if not user_input:
            self.label_widget.configure(text="Введите имя файла", text_color="red")
            self.label_widget.place(x=336, y=150)
            return

        try:
            input_file = "conversations.json"
            chat_input_name = user_input
            output_file = "chat_export.txt"

            Utils.extract_chat(input_file, chat_input_name, output_file, label_widget, extra_label)

        except Exception as er:
            self.label_widget.configure(text="error", text_color="red")
            self.label_widget.place(x=383, y=150)
            msgb(f"{er}", "gptchc-error")

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
            self.label_widget.place(x=340, y=150)
            return
        if len(parts) != 3:
            self.label_widget.configure(text_color="yellow", text="title, icon_type, text")
            self.label_widget.place(x=340, y=150)
            return

        try:
            title = parts[0]
            icon_type = parts[1].lower()
            text = parts[2]

            icon_code = notify_icons.get(icon_type, 0x10)

            self.label_widget.configure(text="Notification was shown", text_color="#00CF00")
            self.label_widget.place(x=328, y=150)

            threading.Thread(target=Utils.show_messagebox, args=(text, title, icon_code), daemon=True).start()

        except Exception as error_ctypes:
            self.label_widget.configure(text=f"error\n{error_ctypes}", text_color="red")
            self.label_widget.pack()
            msgb(f"{error_ctypes}", "notify-error")
