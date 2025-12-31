try:
    import customtkinter as ctk
    from faker import Faker
    from colorama import Fore, Style, init
except ModuleNotFoundError:
    import subprocess
    import sys

    boot_path = "../boot_loader.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()
init(autoreset=True)
faker_frame = None
def faker_ru(frame):
    for widget in frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()

    copyable = ctk.CTkTextbox(
        frame,
        width=500,
        height=320,
        fg_color="black",
        text_color="white",
        font=("Arial", 14),
        wrap="word"
    )
    copyable.pack(padx=20, pady=20)
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER]{Fore.RESET} {Fore.MAGENTA}Russian{Fore.RESET}:  Fake information  | {Fore.LIGHTGREEN_EX}was shown")

    fake = Faker('Ru_ru')

    text = f"""
    name: {fake.name()}\n
    address: {fake.address()}\n
    city: {fake.city()}\n
    phone number: {fake.phone_number()}\n
    email: {fake.email()}\n
    ssn: {fake.ssn()}\n
    password: {fake.password()}\n
    ip: {fake.ipv4()}\n
    """
    copyable.insert("1.0", text)
    copyable.bind("<Key>", lambda s: "break")
    copyable.configure(cursor="arrow")

def faker_eng(frame):
    for widget in frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()

    copyable = ctk.CTkTextbox(
        frame,
        width=400,
        height=320,
        fg_color="black",
        text_color="white",
        font=("Arial", 14),
        wrap="word"
    )
    copyable.pack(padx=20, pady=20)
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER]{Fore.RESET} {Fore.MAGENTA}English{Fore.RESET}:  Fake information  | {Fore.LIGHTGREEN_EX}was shown")

    fake = Faker()

    text = f"""
    name: {fake.name()}\n
    address: {fake.address()}\n
    city: {fake.city()}\n
    phone number: {fake.phone_number()}\n
    email: {fake.email()}\n
    ssn: {fake.ssn()}\n
    password: {fake.password()}\n
    ip: {fake.ipv4()}\n
    """
    copyable.insert("1.0", text)
    copyable.bind("<Key>", lambda s: "break")
    copyable.configure(cursor="arrow")

def faker_es(frame):
    for widget in frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()

    copyable = ctk.CTkTextbox(
        frame,
        width=400,
        height=320,
        fg_color="black",
        text_color="white",
        font=("Arial", 14),
        wrap="word"
    )
    copyable.pack(padx=20, pady=20)
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER]{Fore.RESET} {Fore.MAGENTA}Spanish{Fore.RESET}:  Fake information  | {Fore.LIGHTGREEN_EX}was shown")

    fake = Faker('es_ES')

    text = f"""
    name: {fake.name()}\n
    address: {fake.address()}\n
    city: {fake.city()}\n
    phone number: {fake.phone_number()}\n
    email: {fake.email()}\n
    ssn: {fake.ssn()}\n
    password: {fake.password()}\n
    ip: {fake.ipv4()}\n
    """
    copyable.insert("1.0", text)
    copyable.bind("<Key>", lambda s: "break")
    copyable.configure(cursor="arrow")

def faker_jp(frame):
    for widget in frame.pack_slaves():
        if isinstance(widget, ctk.CTkTextbox):
            widget.destroy()

    copyable = ctk.CTkTextbox(
        frame,
        width=600,
        height=320,
        fg_color="black",
        text_color="white",
        font=("Arial", 14),
        wrap="word"
    )
    copyable.pack(padx=20, pady=20)
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER]{Fore.RESET} {Fore.MAGENTA}Japanese{Fore.RESET}: Fake information  | {Fore.LIGHTGREEN_EX}was shown")

    fake = Faker('ja_JP')

    text = f"""
    name: {fake.name()}\n
    address: {fake.address()}\n
    city: {fake.city()}\n
    phone number: {fake.phone_number()}\n
    email: {fake.email()}\n
    ssn: {fake.ssn()}\n
    password: {fake.password()}\n
    ip: {fake.ipv4()}\n
    """
    copyable.insert("1.0", text)
    copyable.bind("<Key>", lambda s: "break")
    copyable.configure(cursor="arrow")