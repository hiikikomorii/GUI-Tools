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
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER: RU]{Style.NORMAL} {Fore.LIGHTGREEN_EX}fake information was shown")

    fake = Faker('Ru_ru')

    ipv4f = fake.ipv4()
    addressf = fake.address()
    namef = fake.name()
    phonef = fake.phone_number()
    emailf = fake.email()
    ssnf = fake.ssn()
    cityf = fake.city()
    passwf = fake.password()

    text = f"""
    name: {namef}\n
    address: {addressf}\n
    city: {cityf}\n
    phone number: {phonef}\n
    email: {emailf}\n
    ssn: {ssnf}\n
    password: {passwf}\n
    ip: {ipv4f}\n
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
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER: ENG]{Style.NORMAL} {Fore.LIGHTGREEN_EX}fake information was shown")

    fake = Faker()

    ipv4f = fake.ipv4()
    addressf = fake.address()
    namef = fake.name()
    phonef = fake.phone_number()
    emailf = fake.email()
    ssnf = fake.ssn()
    cityf = fake.city()
    passwf = fake.password()

    text = f"""
    name: {namef}\n
    address: {addressf}\n
    city: {cityf}\n
    phone number: {phonef}\n
    email: {emailf}\n
    ssn: {ssnf}\n
    password: {passwf}\n
    ip: {ipv4f}\n
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
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER: ES]{Style.NORMAL} {Fore.LIGHTGREEN_EX}fake information was shown")

    fake = Faker('es_ES')

    ipv4f = fake.ipv4()
    addressf = fake.address()
    namef = fake.name()
    phonef = fake.phone_number()
    emailf = fake.email()
    ssnf = fake.ssn()
    cityf = fake.city()
    passwf = fake.password()

    text = f"""
    name: {namef}\n
    address: {addressf}\n
    city: {cityf}\n
    phone number: {phonef}\n
    email: {emailf}\n
    ssn: {ssnf}\n
    password: {passwf}\n
    ip: {ipv4f}\n
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
    print(f"{Fore.BLUE}{Style.BRIGHT}[FAKER: JP]{Style.NORMAL} {Fore.LIGHTGREEN_EX}fake information was shown")

    fake = Faker('ja_JP')

    ipv4f = fake.ipv4()
    addressf = fake.address()
    namef = fake.name()
    phonef = fake.phone_number()
    emailf = fake.email()
    ssnf = fake.ssn()
    cityf = fake.city()
    passwf = fake.password()

    text = f"""
    name: {namef}\n
    address: {addressf}\n
    city: {cityf}\n
    phone number: {phonef}\n
    email: {emailf}\n
    ssn: {ssnf}\n
    password: {passwf}\n
    ip: {ipv4f}\n
    """
    copyable.insert("1.0", text)
    copyable.bind("<Key>", lambda s: "break")
    copyable.configure(cursor="arrow")