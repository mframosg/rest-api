# Proyecto REST API

Este es un proyecto de API REST desarrollado utilizando Django.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:
- **Python**: Este proyecto requiere Python 3.8 o superior. Verifica tu versión de Python con el comando `python --version`. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).

## Configuración del entorno

Sigue estos pasos para configurar tu entorno de desarrollo:

1. **Clonar el repositorio**:
    - Con **Git** instalado, abre una terminal y ejecuta:
      ```bash
      git clone https://github.com/mframosg/GraphQL-API.git
      ```
    - Sin Git, descarga el repositorio como ZIP desde GitHub y descomprímelo localmente.

2. **Crear y activar un entorno virtual**:
    - Instala `virtualenv`:
      ```bash
      pip install virtualenv
      ```
    - Crea y activa un entorno virtual:
      - **Windows**:
        ```bash
        virtualenv myenv
        myenv\Scripts\activate
        ```
      - **Unix/MacOS**:
        ```bash
        virtualenv myenv
        source myenv/bin/activate
        ```

3. **Instalar dependencias**:
    - Con el entorno activo, instala las dependencias:
      ```bash
      pip install -r requirements.txt
      ```

4. **Configurar variables de entorno**:
    - Crea un `.env` en el directorio raíz para las configuraciones sensibles:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=nombre_de_usuario
      DATABASE_PASSWORD=contraseña
      DATABASE_HOST=dirección_del_host
      DATABASE_PORT=número_de_puerto
      SECRET_KEY=tu_clave_secreta_de_django
      DEBUG=True # o False, en producción
      ```
    - Reemplaza los placeholders con tus datos.

## Configuración de la Base de Datos MySQL

Antes de ejecutar la aplicación, asegúrate de tener MySQL instalado y configurado:

1. **Instalación de MySQL Workbench**: Descarga e instala desde [el sitio web oficial de MySQL](https://www.mysql.com/products/workbench/).

2. **Creación de la base de datos**: Usa MySQL Workbench o la línea de comandos para crear tu base de datos.

3. **Configuración en Django**: Asegúrate de que las credenciales en `.env` coincidan con tu configuración de MySQL.

## Ejecución del proyecto

1. **Ejecutar el servidor de desarrollo**:
    - Inicia el servidor:
      ```bash
      python manage.py runserver
      ```

## Endpoint Adicional

- **/fill_table/**: Este endpoint permite llenar la base de datos. Accede a él después de configurar la base de datos y antes de realizar consultas.

