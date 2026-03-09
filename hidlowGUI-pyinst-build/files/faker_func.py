try:
    import customtkinter as ctk
    from faker import Faker
except ModuleNotFoundError:
    pass

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
            width=450,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.place(x=180, y=10)

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
            width=450,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.place(x=180, y=10)

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
            width=450,
            height=320,
            fg_color="black",
            text_color="white",
            font=("Arial", 14),
            wrap="word"
        )
        self.copyable.place(x=180, y=10)

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
        self.copyable.place(x=180, y=10)

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
