try:
    import customtkinter as ctk
    from faker import Faker
    from colorama import Fore, Style, init
except ModuleNotFoundError:
    import subprocess
    import sys

    boot_path = "bootstrapper.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

init(autoreset=True)
class Main_faker:
    def __init__(self, frame, copyable):
        self.frame = frame
        self.copyable = copyable

    def faker_ru(self, frame):
        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        self.copyable = ctk.CTkTextbox(
            frame,
            width=500,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.pack(padx=20, pady=20)
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
        self.copyable.insert("1.0", text)
        self.copyable.bind("<Key>", lambda s: "break")
        self.copyable.configure(cursor="arrow")

    def faker_eng(self, frame):
        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        self.copyable = ctk.CTkTextbox(
            frame,
            width=500,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.pack(padx=20, pady=20)
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
        self.copyable.insert("1.0", text)
        self.copyable.bind("<Key>", lambda s: "break")
        self.copyable.configure(cursor="arrow")

    def faker_es(self, frame):
        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        self.copyable = ctk.CTkTextbox(
            frame,
            width=500,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.pack(padx=20, pady=20)
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
        self.copyable.insert("1.0", text)
        self.copyable.bind("<Key>", lambda s: "break")
        self.copyable.configure(cursor="arrow")

    def faker_jp(self, frame):
        for widget in frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        self.copyable = ctk.CTkTextbox(
            frame,
            width=500,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.pack(padx=20, pady=20)
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
        self.copyable.insert("1.0", text)
        self.copyable.bind("<Key>", lambda s: "break")
        self.copyable.configure(cursor="arrow")

class Main_test:
    def __init__(self, master):
        self.root = master
        self.root.title("faker-example")
        self._widgets()
        self.all_fakers = Main_faker(self.example_faker_frame, self.copyable)

    def _widgets(self):
        self.copyable = ctk.CTkTextbox(self.root)
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack()

        self.example_faker_frame = ctk.CTkFrame(self.root)

        self.btn_1 = ctk.CTkButton(self.main_frame, text="Russian", width=50, command=self.prepare_faker_ru)
        self.btn_1.pack(side="left", padx=5)

        self.btn_2 = ctk.CTkButton(self.main_frame, text="English", width=50, command=self.prepare_faker_eng)
        self.btn_2.pack(side="left", padx=5)

        self.btn_3 = ctk.CTkButton(self.main_frame, text="Spanish", width=50, command=self.prepare_faker_es)
        self.btn_3.pack(side="left", padx=5)

        self.btn_4 = ctk.CTkButton(self.main_frame, text="Japanese", width=50, command=self.prepare_faker_jp)
        self.btn_4.pack(side="left", padx=5)

        self.back_btn = ctk.CTkButton(self.example_faker_frame, text="back", text_color="red", width=50, command=self.go_back)
        self.back_btn.pack(pady=5)

    def prepare_faker_ru(self):
        self.main_frame.pack_forget()
        self.example_faker_frame.pack()
        self.all_fakers.faker_ru(self.example_faker_frame)

    def prepare_faker_eng(self):
        self.main_frame.pack_forget()
        self.example_faker_frame.pack()
        self.all_fakers.faker_eng(self.example_faker_frame)

    def prepare_faker_es(self):
        self.main_frame.pack_forget()
        self.example_faker_frame.pack()
        self.all_fakers.faker_es(self.example_faker_frame)

    def prepare_faker_jp(self):
        self.main_frame.pack_forget()
        self.example_faker_frame.pack()
        self.all_fakers.faker_jp(self.example_faker_frame)

    def go_back(self):
        for widget in self.example_faker_frame.pack_slaves():
            if isinstance(widget, ctk.CTkTextbox):
                widget.destroy()

        self.example_faker_frame.pack_forget()
        self.main_frame.pack()


if __name__ == '__main__':
    root = ctk.CTk()
    app = Main_test(root)
    root.mainloop()