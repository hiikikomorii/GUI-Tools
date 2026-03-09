try:
    import requests
    import customtkinter as ctk
    import ctypes
except ModuleNotFoundError:
    pass

def msgb(text, title):
    threading.Thread(target=lambda: ctypes.windll.user32.MessageBoxW(0, text, title, 0x10), daemon=True).start()

class Api:
    def __init__(self, copyable, label_widgets):
        self.copyable = copyable
        self.label_widgets = label_widgets

    def select_ton(self, frame):
        try:
            for widget in frame.pack_slaves():
                if isinstance(widget, ctk.CTkTextbox):
                    widget.destroy()

            self.copyable = ctk.CTkTextbox(
                frame,
                width=170,
                height=80,
                fg_color="black",
                text_color="white",
                font=("Arial", 14),
                wrap="word"
            )
            self.copyable.pack(side="top", anchor="center", pady=20)

            url = "https://api.coinpaprika.com/v1/tickers/toncoin-the-open-network?quotes=USD,RUB"
            response = requests.get(url, headers={"User-Agent": "TkinterApp"})
            data = response.json()

            quo = data.get("quotes", {})
            usd = quo.get("USD", {})
            rub = quo.get("RUB", {})

            tonusd = usd.get("price", "не найдено")
            tonrub = rub.get("price", "не найдено")

            text = (
                f"Криптовалюта: TON\n"
                f"Цена в USD: {tonusd:.2f} $\n"
                f"Цена в RUB: {tonrub:.1f} ₽"
            )

            self.copyable.insert("1.0", text)
            self.copyable.bind("<Key>", lambda s: "break")
            self.copyable.configure(cursor="arrow")

        except Exception as error_ton:
            msgb(f"{error_ton}", "ton-error")

    def select_btc(self, frame):
        try:
            for widget in frame.pack_slaves():
                if isinstance(widget, ctk.CTkTextbox):
                    widget.destroy()

            self.copyable = ctk.CTkTextbox(
                frame,
                width=195,
                height=80,
                fg_color="black",
                text_color="white",
                font=("Arial", 14),
                wrap="word"
            )
            self.copyable.pack(side="top", anchor="center", pady=20)

            url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin?quotes=USD,RUB"
            response = requests.get(url, headers={"User-Agent": "TkinterApp"})
            data = response.json()

            quo = data.get("quotes", {})
            usd = quo.get("USD", {})
            rub = quo.get("RUB", {})

            btcusd = usd.get("price", "not found")
            btcrub = rub.get("price", "not found")

            text = (
                f"Криптовалюта: BTC\n"
                f"Цена в USD: {btcusd:.2f} $\n"
                f"Цена в RUB: {btcrub:.1f} ₽"
            )

            self.copyable.insert("1.0", text)
            self.copyable.bind("<Key>", lambda s: "break")
            self.copyable.configure(cursor="arrow")

        except Exception as error_btc:
            msgb(f"{error_btc}", "btc-error")



    def api_ip(self, entry_widgets, label_widgets, frame, cp_btn, accept, back, clear, paste):
        user_input = entry_widgets.get().strip()
        label_widgets.pack_forget()

        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        if not user_input:
            label_widgets.configure(text="Введите IP", text_color="red")
            label_widgets.place(x=365, y=130)
            return

        try:
            self.copyable = ctk.CTkTextbox(
                frame,
                width=350,
                height=400,
                fg_color="black",
                text_color="white",
                font=("Arial", 14),
                wrap="word"
            )
            self.copyable.pack(anchor="center", side="top", pady=10)

            response = requests.get(f"https://ipwhois.app/json/{user_input}")
            data = response.json()

            if data.get("message"):
                self.copyable.insert("1.0", f"{data.get('message', 'Ошибка')}")
                clear.place(x=10, y=10)
                back.place(x=10, y=50)
                return

            text = (
                f"IP: {data.get('ip', 'не найдено')}\n"
                f"Тип: {data.get('type', 'не найдено')}\n"
                f"Долгота: {data.get('latitude', 'не найдено')}\n"
                f"Широта: {data.get('longitude', 'не найдено')}\n"
                f"Континент: {data.get('continent', 'не найдено')}\n"
                f"Страна: {data.get('country', 'не найдено')}\n"
                f"Столица: {data.get('country_capital', 'не найдено')}\n"
                f"Регион: {data.get('region', 'не найдено')}\n"
                f"Город: {data.get('city', 'не найдено')}\n"
                f"Соседние страны: {data.get('country_neighbours', 'не найдено')}\n"
                f"Флаг: {data.get('country_flag', 'не найдено')}\n"
                f"Код телефона: {data.get('country_phone', 'не найдено')}\n"
                f"Код континента: {data.get('continent_code', 'не найдено')}\n"
                f"Код страны: {data.get('country_code', 'не найдено')}\n"
                f"Код валюты: {data.get('currency_code', 'не найдено')}\n"
                f"ASN: {data.get('asn', 'не найдено')}\n"
                f"Провайдер: {data.get('isp', 'не найдено')}\n"
                f"Организация: {data.get('org', 'не найденo')}\n"
                f"Часовой пояс: {data.get('timezone', 'не найдено')}\n"
                f"Название: {data.get('timezone_name', 'не найдено')}\n"
                f"Валюта: {data.get('currency', 'не найдено')}\n"
                f"Символ валюты: {data.get('currency_symbol', 'не найдено')}\n"

            )

            def copy_text():
                frame.clipboard_clear()
                frame.clipboard_append(self.copyable.get("1.0", "end-1c"))
                frame.update()
                cp_btn.configure(text_color="#00CF00")

            cp_btn.configure(command=copy_text)
            entry_widgets.place_forget()
            paste.place_forget()
            accept.place_forget()
            cp_btn.place(x=10, y=10)
            clear.place(x=10, y=50)
            back.place(x=10, y=90)


            self.copyable.insert("1.0", text)
            self.copyable.configure(state="normal")

        except Exception as er:
            label_widgets.configure(text=f"Ошибка API-IP: {er}", text_color="red")
            label_widgets.pack()
            msgb(f"{er}", "ip-error")

    def api_lat(self, entry_widgets, label_widgets, frame, cp_btn, accept, back, clear, paste):
        user_input = entry_widgets.get().strip()
        label_widgets.pack_forget()

        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        if not user_input:
            label_widgets.configure(text="Введите координаты (lat | lon)", text_color="red")
            label_widgets.place(x=310, y=130)
            return

        try:
            parts = user_input.split()

            if len(parts) != 2:
                label_widgets.configure(text="введите два значения: широта и долгота через пробел", text_color="red")
                label_widgets.place(x=235, y=130)
                return

            lat, lon = parts

            self.copyable = ctk.CTkTextbox(
                frame,
                width=300,
                height=350,
                fg_color="black",
                text_color="white",
                font=("Arial", 14),
                wrap="word"
            )
            self.copyable.pack(anchor="center", side="top", pady=10)

            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
            response = requests.get(url, headers={"User-Agent": "TkinterApp"})
            data = response.json()

            if data.get('error'):
                copyable.insert("1.0", f"{data.get('error', 'Ошибка')}")
                clear.place(x=10, y=10)
                back.place(x=10, y=50)
                return

            text = (
                f"Страна: {data.get('address', {}).get('country', 'не найдено')}\n"
                f"Регион: {data.get('address', {}).get('region', 'не найдено')}\n"
                f"Область: {data.get('address', {}).get('state', 'не найдено')}\n"
                f"Город: {data.get('address', {}).get('city', data.get('address', {}).get('town', 'не найдено'))}\n"
                f"Пригород: {data.get('address', {}).get('suburb', 'не найдено')}\n"
                f"Квартал: {data.get('address', {}).get('quarter', 'не найдено')}\n"
                f"Улица: {data.get('address', {}).get('road', 'не найдено')}\n"
                f"Микрорайон: {data.get('address', {}).get('neighbourhood', 'не найдено')}\n"
                f"Достопримечательность: {data.get('address', {}).get('name', 'не найдено')}\n"
                f"Номер дома: {data.get('address', {}).get('house_number', 'не найдено')}\n\n"
                f"Код страны: {data.get('address', {}).get('country_code', 'не найдено')}\n"
                f"ID места: {data.get('place_id', 'не найдено')}\n"
                f"Тип объекта: {data.get('osm_type', 'не найдено')}\n"
                f"Класс объекта: {data.get('class', 'не найдено')}\n"
                f"Тип: {data.get('type', 'не найдено')}\n"
                f"Почтовый индекс: {data.get('address', {}).get('postcode', 'не найдено')}\n"

            )

            def copy_text():
                frame.clipboard_clear()
                frame.clipboard_append(self.copyable.get("1.0", "end-1c"))
                frame.update()
                cp_btn.configure(text_color="#00CF00")

            cp_btn.configure(command=copy_text)
            entry_widgets.place_forget()
            paste.place_forget()
            accept.place_forget()
            cp_btn.place(x=10, y=10)
            clear.place(x=10, y=50)
            back.place(x=10, y=90)

            self.copyable.insert("1.0", text)
            self.copyable.configure(state="normal")

        except Exception as er:
            label_widgets.configure(text=f"Ошибка API-lat: {er}", text_color="red")
            label_widgets.pack()
            msgb(f"{er}", "geo-error")