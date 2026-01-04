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
        width=400,
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


def example_test():
    root = ctk.CTk()
    main_frame = ctk.CTkFrame(root)
    main_frame.pack()

    example_faker_frame = ctk.CTkFrame(root)

    def prepare_faker_ru():
        main_frame.pack_forget()
        example_faker_frame.pack()
        faker_ru(example_faker_frame)

    def prepare_faker_eng():
        main_frame.pack_forget()
        example_faker_frame.pack()
        faker_eng(example_faker_frame)

    def prepare_faker_es():
        main_frame.pack_forget()
        example_faker_frame.pack()
        faker_es(example_faker_frame)

    def prepare_faker_jp():
        main_frame.pack_forget()
        example_faker_frame.pack()
        faker_jp(example_faker_frame)

    def go_back():
        for widget in example_faker_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        example_faker_frame.pack_forget()
        main_frame.pack()



    btn_1 = ctk.CTkButton(main_frame, text="Russian", width=50, command=prepare_faker_ru)
    btn_1.pack(side="left", padx=5)

    btn_2 = ctk.CTkButton(main_frame, text="English", width=50, command=prepare_faker_eng)
    btn_2.pack(side="left", padx=5)

    btn_3 = ctk.CTkButton(main_frame, text="Spanish", width=50, command=prepare_faker_es)
    btn_3.pack(side="left", padx=5)

    btn_4 = ctk.CTkButton(main_frame, text="Japanese", width=50, command=prepare_faker_jp)
    btn_4.pack(side="left", padx=5)

    back_btn = ctk.CTkButton(example_faker_frame, text="back", text_color="red", width=50, command=go_back)
    back_btn.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    example_test()