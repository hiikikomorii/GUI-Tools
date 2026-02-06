import time
import subprocess
import os
import sys

try:
    f = open('../requirements.txt', 'r')
    print("../")
except FileNotFoundError:
    f = open('assets/requirements.txt', 'r')
    print('files/')

def typ(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

typ("\rHello!\n", delay=0.05)
time.sleep(1)
typ("Modules:", delay=0.03)
typ(f"{f.read()}", delay=0.02)
f.close()
time.sleep(0.5)

try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd="assets")
except Exception as e:
    print(f"ERROR\n" * 5 + e)
    input('enter: ')

os.system('cls')
typ("Done!", delay=0.03)
typ("Starting HidlowToolsGUI", delay=0.03)

try:
    boot_path = "bootstrapper.py"
    subprocess.Popen(
        ["cmd", "/c", sys.executable, str(boot_path)],
        cwd="files/bootstrapper",
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()
except Exception as e:
    print(e)
