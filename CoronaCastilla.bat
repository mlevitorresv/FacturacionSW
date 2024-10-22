@echo off
REM Cambia al directorio del proyecto
cd .\FacturacionSW\

REM Ejecuta el servidor Django en segundo plano
start "" python manage.py runserver

REM Espera de 5 segundos para asegurar que el servidor está en funcionamiento
timeout /t 5 /nobreak >nul

REM Abre el navegador en la dirección del poryecto django
start python run_app.py