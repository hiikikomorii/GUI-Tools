try:
    import re
    import phonenumbers
    import random
    import time
    import requests
    import customtkinter as ctk
    import threading
    import ctypes

except ModuleNotFoundError as e:
    pass


def msgb(text, title):
    threading.Thread(target=lambda: ctypes.windll.user32.MessageBoxW(0, text, title, 0x10), daemon=True).start()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/119.0",
]

headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "TE": "Trailers"
}


class Api:
    def __init__(self, label_wd):
        self.label_wd = label_wd

    @staticmethod
    def send_request(url, phone):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            time.sleep(random.uniform(2, 5))
            if response.status_code == 200:
                return response.json()
            else:
                msgb(f"{phone}\n{response.status_code}", "number-error")
                return None
        except Exception as er:
            msgb(f"{er}", "number-error")
            return None

    def api_number(self, entry_wd, label_wd, frame, cp_btn, accept, back, clear, paste):
        user_input = entry_wd.get().strip()
        self.label_wd.pack_forget()
        self.label_wd.configure(text="wait..", text_color="white")
        self.label_wd.pack(side="bottom", anchor="center", pady=20)
        if not user_input:
            self.label_wd.configure(text="Введите номер телефона!", text_color="red")
            self.label_wd.place(x=320, y=130)
            return

        try:
            copyable = ctk.CTkTextbox(
                frame,
                width=600,
                height=300,
                fg_color="black",
                text_color="white",
                font=("Arial", 14),
                wrap="word"
            )
            copyable.pack(anchor="center", side="top", pady=10)

            def paste_text(_=None):
                copyable.configure(state="normal")
                copyable.event_generate("<<Paste>>")
                copyable.configure(state="normal")
                return "break"

            url = f"https://htmlweb.ru/geo/api.php?json&telcod={user_input}"
            data = Api.send_request(url, user_input)

            if not data or not isinstance(data, dict):
                copyable.insert("1.0", "[!] Ошибка: не удалось получить данные.")
                clear.place(x=10, y=10)
                back.place(x=10, y=50)
                return

            if data.get("status_error"):
                copyable.insert("1.0", f"Ошибка API: {data.get('error_message', 'Не удалось получить данные.')}")
                clear.place(x=10, y=10)
                back.place(x=10, y=50)
                return

            if data.get("limit") is not None and data.get("limit") <= 0:
                copyable.insert("1.0", "Ошибка: лимит запросов исчерпан.")
                clear.place(x=10, y=10)
                back.place(x=10, y=50)
                return

            country = data.get('country', {}) or {}
            region = data.get('region', {}) or {}
            capital = data.get('capital', {}) or {}

            text = (
                f"Номер телефона: {user_input}\n"
                f"Страна: {country.get('name', 'Не найдено')} ({country.get('fullname', '—')})\n"
                f"Регион: {region.get('name', 'Не найдено')}\n"
                f"Город: {capital.get('name', 'Не найдено')}\n"
                f"Почтовый индекс: {capital.get('post', 'Не найдено')}\n"
                f"Код валюты: {country.get('iso', 'Не найдено')}\n"
                f"Телефонный код: {capital.get('telcod', 'Не найдено')}\n"
                f"Оператор: {capital.get('oper_brand', 'Не найдено')} ({capital.get('def', 'Не найдено')})\n"
                f"Столица: {capital.get('name', 'Не найдено')}\n"
                f"Широта / Долгота: {capital.get('latitude', '—')}, {capital.get('longitude', '—')}\n"
                f"Wiki: {capital.get('wiki', '—')}\n"
                f"Автокод региона: {region.get('autocod', '—')}\n"
                f"Локация: {country.get('location', '—')}\n"
                f"Язык: {country.get('lang', '—')}\n"
                f"Google Maps: https://www.google.com/maps/place/{capital.get('latitude', '')}+{capital.get('longitude', '')}\n"
                f"Рейтинг номера: https://phoneradar.ru/phone/{user_input}\n"
            )

            def copy_text():
                try:
                    frame.clipboard_clear()
                    frame.clipboard_append(copyable.get("1.0", "end-1c"))
                    frame.update()
                    cp_btn.configure(text_color="#00CF00")
                except Exception:
                    pass

            cp_btn.configure(command=copy_text)
            entry_wd.place_forget()
            paste.place_forget()
            accept.place_forget()
            cp_btn.place(x=10, y=10)
            clear.place(x=10, y=50)
            back.place(x=10, y=90)

            copyable.insert("1.0", text)
            copyable.bind("<Control-v>", paste_text)
            label_wd.pack_forget()

        except Exception as er:
            msgb(f"{er}", "error-nb")
            self.label_wd.configure(text=f"Ошибка API: {er}", text_color="red")
            self.label_wd.pack()
