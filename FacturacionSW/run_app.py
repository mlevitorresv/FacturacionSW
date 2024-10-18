import webview
import subprocess

subprocess.Popen(['python', 'manage.py', 'runserver'])

webview.create_window('Facturación SW', 'http://localhost:8000')
webview.start()