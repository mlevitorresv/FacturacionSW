import webview
import subprocess
import time
import os
import requests

# Función para iniciar el servidor Django
def start_django_server():
    subprocess.Popen(['python', 'manage.py', 'runserver'])

def wait_for_django_server(url, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            time.sleep(0.5)
    return False


django_url = 'http://localhost:8000'

if __name__ == '__main__':
    start_django_server()

    if wait_for_django_server(django_url):
        webview.create_window('FacturacionSW', django_url)
        webview.start()
