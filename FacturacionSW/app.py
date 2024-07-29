import webview
import subprocess
import time

# Inicia el servidor de desarrollo de Django
subprocess.Popen(["python", "manage.py", "runserver"])

# Espera a que el servidor esté en funcionamiento
time.sleep(5)

# Crea una ventana con PyWebview y carga tu aplicación Django
webview.create_window('Mi App Django', 'http://localhost:8000')
webview.start()
