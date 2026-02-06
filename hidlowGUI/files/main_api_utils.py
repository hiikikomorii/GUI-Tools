try:
    from colorama import init, Fore, Style
    import requests
    import customtkinter as ctk

except ModuleNotFoundError:
    import subprocess
    import sys
    boot_path = "bootstrapper/bootstrapper.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

init(autoreset=True)

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
            self.copyable.pack(padx=20, pady=20)
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} TON currency: {Fore.LIGHTGREEN_EX}was shown")

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
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RED} TON ERROR\napi недоступно\n{error_ton}")

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
            self.copyable.pack(padx=20, pady=20)
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} BTC currency: {Fore.LIGHTGREEN_EX}was shown")

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
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RED} BTC ERROR\napi недоступно\n{error_btc}")

    def api_ip(self, entry_widgets, label_widgets, frame, cp_btn):
        user_input = entry_widgets.get().strip()
        label_widgets.pack_forget()

        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        if not user_input:
            label_widgets.configure(text="Введите IP", text_color="red")
            label_widgets.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} IP: {Fore.LIGHTYELLOW_EX}was not entered")
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
            self.copyable.pack(padx=20, pady=20)

            response = requests.get(f"https://ipwhois.app/json/{user_input}")
            data = response.json()

            if data.get("message"):
                self.copyable.insert("1.0", f"{data.get('message', 'Ошибка')}")
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

            self.copyable.insert("1.0", text)
            self.copyable.configure(state="normal")
            frame.pack(pady=10)
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} IP: {Fore.MAGENTA}{user_input}{Fore.RESET} | {Fore.LIGHTGREEN_EX}True")

        except Exception as er:
            label_widgets.configure(text=f"Ошибка API-IP: {er}", text_color="red")
            label_widgets.pack()
            print(f"{Fore.BLUE}{Style.BRIGHT}[API] {Fore.LIGHTRED_EX}Ошибка API-IP: {er}")

    def api_lat(self, entry_widgets, label_widgets, frame, cp_btn):
        user_input = entry_widgets.get().strip()
        label_widgets.pack_forget()

        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        if not user_input:
            label_widgets.configure(text="Введите координаты (lat lon)", text_color="red")
            label_widgets.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} GEO: {Fore.LIGHTYELLOW_EX}was not entered")
            return

        try:
            parts = user_input.split()

            if len(parts) != 2:
                label_widgets.configure(text="Введите два значения: широта и долгота через пробел", text_color="red")
                label_widgets.pack(pady=5)
                print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} GEO: {Fore.LIGHTYELLOW_EX}were entered incorrectly")
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
            self.copyable.pack(padx=20, pady=20)

            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
            response = requests.get(url, headers={"User-Agent": "TkinterApp"})
            data = response.json()

            if data.get('error'):
                copyable.insert("1.0", f"{data.get('error', 'Ошибка')}")
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

            self.copyable.insert("1.0", text)
            self.copyable.configure(state="normal")
            frame.pack(pady=10)

            print(f"{Fore.BLUE}{Style.BRIGHT}[API]{Fore.RESET} GEO: {Fore.MAGENTA}{lat} {lon}{Fore.RESET} | {Fore.LIGHTGREEN_EX} True")

        except Exception as er:
            label_widgets.configure(text=f"Ошибка API-lat: {er}", text_color="red")
            label_widgets.pack()
            print(f"{Fore.BLUE}{Style.BRIGHT}[API] {Fore.LIGHTRED_EX}Ошибка API-lat: {er}")

class Main:
    def __init__(self, master):
        self.root = master
        self._widgets()
        self.main_api = Api(self.copyable, self.label)

    def _widgets(self):
        self.copyable = ctk.CTkTextbox(self.root)
        self.entry_frame = ctk.CTkFrame(self.root, width=200, height=30, fg_color="#242424")

        self.entry = ctk.CTkEntry(self.entry_frame)
        self.entry.pack(pady=5)

        self.confirm_button = ctk.CTkButton(self.entry_frame, text="OK", text_color="#00CF00", width=80)
        self.confirm_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self.entry_frame, text="Back", text_color="red", width=80, command=self.go_back_from_entry)
        self.back_button.pack()

        self.label = ctk.CTkLabel(self.root, fg_color="#242424")

        self.currency_frame = ctk.CTkFrame(self.root, fg_color="#242424")

        self.main_frame = ctk.CTkFrame(self.root, fg_color="#242424")
        self.main_frame.pack(pady=10)

        self.button1 = ctk.CTkButton(self.main_frame, text="Geo", width=50, corner_radius=10, command=self.prepare_geo)
        self.button1.pack(side="left", padx=5)

        self.button2 = ctk.CTkButton(self.main_frame, text="IP", width=50, corner_radius=10, command=self.prepare_ip)
        self.button2.pack(side="left", padx=5)

        self.button3 = ctk.CTkButton(self.main_frame, text="BTC", width=50, corner_radius=10, command=self.prepare_btc)
        self.button3.pack(side="left", padx=5)

        self.button4 = ctk.CTkButton(self.main_frame, text="TON", width=50, corner_radius=10, command=self.prepare_ton)
        self.button4.pack(side="left", padx=5)

        self.cp_btn = ctk.CTkButton(self.entry_frame, text="Copy", width=80)
        self.cp_btn.pack(pady=5)

        self.example_geo_button = ctk.CTkButton(self.entry_frame, text="example", width=80, command=lambda: self.entry.insert(0, "55.7342 37.6129"))
        self.example_geo_button.pack_forget()

        self.example_ip_button = ctk.CTkButton(self.entry_frame, text="example", width=80, command=lambda: self.entry.insert(0, "51.15.84.185"))
        self.example_ip_button.pack_forget()

        self.go_back_currency = ctk.CTkButton(self.currency_frame, text="back", command=self.go_back_from_currency)
        self.go_back_currency.pack()

    def go_back_from_entry(self):
        self.label.pack_forget()
        self.entry_frame.pack_forget()
        self.example_ip_button.pack_forget()
        self.example_geo_button.pack_forget()
        self.main_frame.pack()

    def go_back_from_currency(self):
        self.currency_frame.pack_forget()
        self.main_frame.pack()
        self.label.pack_forget()


    def prepare_input(self, api_func):
        self.entry.delete(0, "end")
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()
        self.main_frame.pack_forget()
        self.entry_frame.pack(pady=10)
        self.confirm_button.configure(command=api_func)

    def prepare_btc(self):
        self.main_frame.pack_forget()
        self.currency_frame.pack()
        self.main_api.select_btc(self.currency_frame)
        self.go_back_currency.pack(pady=10)

    def prepare_ton(self):
        self.main_frame.pack_forget()
        self.currency_frame.pack()
        self.main_api.select_ton(self.currency_frame)
        self.go_back_currency.pack(pady=10)

    def prepare_geo(self):
        self.prepare_input(lambda: self.main_api.api_lat(self.entry, self.label, self.entry_frame, self.cp_btn))
        self.example_geo_button.pack()

    def prepare_ip(self):
        self.prepare_input(lambda: self.main_api.api_ip(self.entry, self.label, self.entry_frame, self.cp_btn))
        self.example_ip_button.pack()

if __name__ == '__main__':
    root = ctk.CTk()
    app = Main(root)
    root.mainloop()