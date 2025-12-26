try:
    from colorama import init, Fore, Style
    import requests
    import customtkinter as ctk

except ModuleNotFoundError as e:
    import subprocess
    import sys
    boot_path = "../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()
init(autoreset=True)


def select_ton(frame):
    try:
        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        copyable = ctk.CTkTextbox(
            frame,
            width=170,
            height=80,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        copyable.pack(padx=20, pady=20)
        print(f"{Fore.BLUE}{Style.BRIGHT}[TON]{Style.NORMAL} {Fore.LIGHTGREEN_EX}TON currency was shown")

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

        copyable.insert("1.0", text)
        copyable.bind("<Key>", lambda s: "break")
        copyable.configure(cursor="arrow")

    except Exception as error_ton:
        print(f"{Fore.BLUE}{Style.BRIGHT}[TON]{Style.NORMAL} {Fore.RED}TON ERROR\napi недоступно\n{error_ton}")

def select_btc(frame):
    try:
        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        copyable = ctk.CTkTextbox(
            frame,
            width=195,
            height=80,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        copyable.pack(padx=20, pady=20)
        print(f"{Fore.BLUE}{Style.BRIGHT}[BTC]{Style.NORMAL} {Fore.LIGHTGREEN_EX}BTC currency was shown")

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

        copyable.insert("1.0", text)
        copyable.bind("<Key>", lambda s: "break")
        copyable.configure(cursor="arrow")

    except Exception as error_btc:
        print(f"{Fore.BLUE}{Style.BRIGHT}[BTC]{Style.NORMAL} {Fore.RED}BTC ERROR\napi недоступно\n{error_btc}")

def api_ip(entry_widgets, label_widgets, frame):
    user_input = entry_widgets.get().strip()

    label_widgets.pack_forget()
    if not user_input:
        label_widgets.configure(text="Введите ip!", text_color="red")
        label_widgets.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[IP]{Style.NORMAL} {Fore.LIGHTYELLOW_EX}IP не был введен")
        return

    try:
        copyable = ctk.CTkTextbox(
            frame,
            width=350,
            height=400,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        copyable.pack(padx=20, pady=20)

        response = requests.get(f"https://ipwhois.app/json/{user_input}")
        data = response.json()


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


        copyable.insert("1.0", text)
        copyable.configure(state="normal")
        print(f"{Fore.BLUE}{Style.BRIGHT}[IP]{Style.NORMAL} {Fore.LIGHTGREEN_EX}Запрос выполнен: {user_input}")

    except Exception as er:
        label_widgets.configure(text=f"Ошибка API-IP: {er}", text_color="red")
        label_widgets.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[IP]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка API-IP: {er}")

def api_lat(entry_widgets, label_widgets, frame):
    user_input = entry_widgets.get().strip()
    label_widgets.pack_forget()
    if not user_input:
        label_widgets.configure(text="Введите координаты (lat lon)", text_color="red")
        label_widgets.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[LatLon]{Style.NORMAL} {Fore.LIGHTYELLOW_EX}Координаты не были введены.")
        return

    try:
        parts = user_input.split()

        if len(parts) != 2:
            label_widgets.configure(text="Введите два значения: широта и долгота через пробел", text_color="red")
            label_widgets.pack(pady=5)
            print(f"{Fore.BLUE}{Style.BRIGHT}[LatLon]{Style.NORMAL} {Fore.LIGHTYELLOW_EX}Координаты были введены неправильно.")
            return

        lat, lon = parts

        copyable = ctk.CTkTextbox(
            frame,
            width=300,
            height=350,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        copyable.pack(padx=20, pady=20)

        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        response = requests.get(url, headers={"User-Agent": "TkinterApp"})
        data = response.json()

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

        copyable.insert("1.0", text)
        copyable.configure(state="normal")

        print(f"{Fore.BLUE}{Style.BRIGHT}[LatLon]{Style.NORMAL} {Fore.LIGHTGREEN_EX}Запрос был выполнен: {parts}")

    except Exception as er:
        label_widgets.configure(text=f"Ошибка API-lat: {er}", text_color="red")
        label_widgets.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[LatLon]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка API-lat: {er}")

