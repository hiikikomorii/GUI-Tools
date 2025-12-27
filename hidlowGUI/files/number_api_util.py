try:
    import re
    import phonenumbers
    import urllib.request
    import random
    import time
    import requests
    from colorama import init, Fore, Style
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

def send_request(url, phone):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        time.sleep(random.uniform(2, 5))
        if response.status_code == 200:
            print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTGREEN_EX}Запрос выполнен успешно: {phone}")
            return response.json()
        else:
            print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка: {response.status_code}")
            return None
    except Exception as er:
        print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка при отправке запроса: {er}")
        return None

def api_number(entry_wd, label_wd, frame):
    user_input = entry_wd.get().strip()
    label_wd.pack_forget()
    label_wd.configure(text="wait..", text_color="white")
    label_wd.pack(pady=5)
    if not user_input:
        label_wd.configure(text="Введите номер телефона!", text_color="red")
        label_wd.pack(pady=5)
        print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTYELLOW_EX}Номер телефона не был введен.")
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
        copyable.pack(padx=20, pady=20)

        def paste_text(_=None):
            copyable.configure(state="normal")
            copyable.event_generate("<<Paste>>")
            copyable.configure(state="normal")
            return "break"

        url = f"https://htmlweb.ru/geo/api.php?json&telcod={user_input}"
        data = send_request(url, user_input)

        if not data or not isinstance(data, dict):
            copyable.insert("1.0", "[!] Ошибка: не удалось получить данные.")
            print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTRED_EX}[!] Ошибка: не удалось получить данные.")
            return

        if data.get("status_error"):
            copyable.insert("1.0", f"Ошибка API: {data.get('error_message', 'Не удалось получить данные.')}")
            print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка API: {data.get('error_message', 'Не удалось получить данные.')}")
            return

        if data.get("limit") is not None and data.get("limit") <= 0:
            copyable.insert("1.0", "Ошибка: лимит запросов исчерпан.")
            print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTRED_EX}Лимит исчерпан!")
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


        copyable.insert("1.0", text)
        copyable.bind("<Control-v>", paste_text)
        label_wd.pack_forget()

    except Exception as er:
        label_wd.configure(text=f"Ошибка API: {er}", text_color="red")
        label_wd.pack()
        print(f"{Fore.BLUE}{Style.BRIGHT}[NUMBER]{Style.NORMAL} {Fore.LIGHTRED_EX}Ошибка API: {er}")