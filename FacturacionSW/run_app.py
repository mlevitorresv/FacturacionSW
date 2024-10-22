import webview
import subprocess
import time
import os

# Función para iniciar el servidor Django
def start_django_server():
    # Si estás en un entorno virtual, asegúrate de que el comando `python` apunte a la versión correcta de Python.
    # Inicia el servidor Django en segundo plano
    subprocess.Popen(['python', 'manage.py', 'runserver'])
    time.sleep(5)  # Esperar 2 segundos para que el servidor Django arranque

# Ruta del servidor local (cambia si usas otro puerto o dominio)
django_url = 'http://localhost:8000'

if __name__ == '__main__':
    # Verificar si ya se está ejecutando el servidor Django
    start_django_server()

    # Crear la ventana de la aplicación
    webview.create_window('FacturacionSW', django_url)
    webview.start()
