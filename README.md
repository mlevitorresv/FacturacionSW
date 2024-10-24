# FacturaciónSW

**FacturaciónSW** es una aplicación de escritorio diseñada para gestionar facturas de manera eficiente. La aplicación permite generar, gestionar y almacenar facturas utilizando una interfaz gráfica moderna basada en Python y un sistema de base de datos SQL para el almacenamiento de información.

## Características

- **Generación de facturas**: Permite crear facturas detalladas con información de habitaciones, precios, impuestos, etc.
- **Interfaz gráfica**: Construida con `pywebview` para ofrecer una experiencia de usuario fluida y amigable.
- **Gestión de clientes**: Añade y gestiona la información de tus clientes.
- **Exportación**: Exporta facturas en formato PDF o impresión directa.
- **Conexión con .NET**: Utiliza `pythonnet` para aprovechar bibliotecas .NET en la aplicación.
- **Base de datos SQL**: Utiliza una base de datos SQL (MySQL) para almacenar las facturas y datos de los clientes.

## Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- **Python 3.12**
- **pywebview**: Para la creación de la ventana de la interfaz gráfica basada en web.
- **pythonnet**: Para la integración con bibliotecas .NET en Windows.
- **SQL (MySQL/PostgreSQL)**: Base de datos para el almacenamiento de facturas.
- **Bottle**: Para la creación de un servidor web ligero que renderiza la interfaz HTML en `pywebview`.
- **SQLAlchemy**: ORM para interactuar con la base de datos SQL.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

1. **Python 3.12.x**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **pip**: Administrador de paquetes de Python, incluido en las versiones recientes de Python.
3. **Base de datos SQL**: Instala y configura una base de datos SQL. Este proyecto es compatible con:

    - [MySQL](https://dev.mysql.com/downloads/) (recomendado)
    - [PostgreSQL](https://www.postgresql.org/download/)

4. **SQL Client**: Necesitarás también un cliente de base de datos o alguna interfaz para manejar la base de datos. Puedes usar herramientas como:

    - MySQL Workbench para MySQL
    - pgAdmin para PostgreSQL

## Instalación

### 1. Clona este repositorio

```bash
git clone https://github.com/tuusuario/facturacionsw.git
cd facturacionsw

### 2. Instala las dependencias necesarias

Para instalar las dependencias del proyecto, puedes usar el archivo `requirements.txt`.

### Instalar desde `requirements.txt`

Si tienes un archivo `requirements.txt`, puedes instalar todas las dependencias de esta manera:

```bash
pip install -r requirements.txt

### 3. Configura la base de datos SQL
# genera un fichero .env del siguiente estilo
DATABASE_NAME=**name**
DATABASE_USER=**user**
DATABASE_PASSWORD=**passsword**
DATABASE_HOST=**host**
DATABASE_PORT=**port**


## Ejecuta la aplicación
```bash
python run_app.py


