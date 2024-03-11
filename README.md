# Proyecto REST API

Este es un proyecto de API REST desarrollado utilizando Django. La API permite realizar peticiones GET sobre una base de datos MySQL para hacer pruebas de grandes volúmenes de datos.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:
- **Python**: Este proyecto requiere Python 3.8 o superior. Verifica tu versión de Python con el comando `python --version`. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).

## Configuración del entorno

Sigue estos pasos para configurar tu entorno de desarrollo:

1. **Clonar el repositorio**:
    - Si tienes **Git** instalado, abre una terminal y ejecuta el siguiente comando para clonar el repositorio:
      ```bash
      git clone https://github.com/mframosg/rest-api.git
      ```
      ```bash
      cd Rest-Api
      ```
    - Si **no** tienes Git, puedes descargar el repositorio como un archivo ZIP desde GitHub y descomprimirlo en tu máquina local.

2. **Crear y activar un entorno virtual**:
    - Instala `virtualenv` si aún no lo has hecho:
      ```bash
      pip install virtualenv
      ```
    - Crea un entorno virtual llamado `myenv` (puedes nombrarlo como prefieras) dentro del directorio del proyecto:
      ```bash
      virtualenv myenv
      ```
    - Activa el entorno virtual:
      - En **Windows**:
        ```bash
        myenv\Scripts\activate
        ```
      - En **Unix/MacOS**:
        ```bash
        source myenv/bin/activate
        ```

3. **Instalar dependencias**:
    - Con el entorno virtual activado, instala las dependencias del proyecto ejecutando:
      ```bash
      pip install -r requirements.txt
      ```
      
## Configuración de MySQL Workbench

Para configurar tu base de datos en MySQL Workbench, sigue estos pasos:

1. **Instala MySQL Workbench**: Descarga e instala MySQL Workbench desde el [sitio web oficial](https://www.mysql.com/products/workbench/).

2. **Conéctate a tu servidor MySQL**: Abre MySQL Workbench y crea una nueva conexión al servidor MySQL donde deseas alojar tu base de datos. Introduce las credenciales de conexión necesarias.

3. **Crea la base de datos**:
    - Abre un nuevo query tab y ejecuta el siguiente comando SQL para crear tu base de datos:
      ```sql
      CREATE DATABASE nombre_de_tu_base_de_datos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
      ```
    - Asegúrate de reemplazar `nombre_de_tu_base_de_datos` con el nombre que deseas para tu base de datos.
    - Ahora seleccionamos nuestra tabla creada:
       ```sql
      USE nombre_de_tu_base_de_datos;
      ```

4. **Crea la tabla necesaria**:
    - Ejecuta el siguiente comando SQL para crear la tabla `usuarios` con el formato especificado:
      ```sql
      CREATE TABLE usuarios (
          idusuario INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(100),
          age INT
      );
      ```
5. **Configurar variables de entorno**:
    - Crea un archivo `.env` en el directorio raíz del proyecto para almacenar configuraciones sensibles, como las credenciales de la base de datos:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=nombre_de_usuario
      DATABASE_PASSWORD=contraseña
      DATABASE_HOST=dirección_del_host #default is localhost
      DATABASE_PORT=número_de_puerto #mysql default is 3306
      ```
    - Asegúrate de reemplazar los valores de placeholder con tus configuraciones reales.


## Ejecución del proyecto

Con tu entorno configurado y las dependencias instaladas, estás listo para ejecutar el proyecto:

1. **Ejecutar el servidor de desarrollo**:
    - Inicia el servidor de desarrollo con:
      ```bash
      python manage.py runserver
      ```

## Documentación adicional

Esta es la primera parte del proyecto. Accede a la segunda parte para hacer pruebas en graphql: [API REST en Django](https://github.com/mframosg/graphql-api).
