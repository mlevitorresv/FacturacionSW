import webview
import subprocess
import time
import os
from pathlib import Path

# Define el directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Cambia al directorio donde está manage.py
os.chdir(BASE_DIR)

# Inicia el servidor de desarrollo de Django
subprocess.Popen(["python", "manage.py", "runserver"], cwd=BASE_DIR)

# Espera a que el servidor esté en funcionamiento
time.sleep(5)

# Crea una ventana con PyWebview y carga tu aplicación Django
webview.create_window('CoronaCastilla', 'http://localhost:8000')
webview.start()
