# Proyecto REST API

Este es un proyecto de API REST desarrollado utilizando Django. La API permite realizar consultas y agregar usuarios sobre una base de datos MySQL, para hacer pruebas de grandes volúmenes de datos.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:
- **Python**: Este proyecto requiere Python 3.8 o superior. Verifica tu versión de Python con el comando `python --version`. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).
- **MySQL Workbench**: Este proyecto utiliza una base de datos MySQL. Necesitarás MySQL Workbench para gestionar la base de datos, disponible en el [sitio web oficial](https://www.mysql.com/products/workbench/).


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
    - Si **NO** tienes Git, descarga el proyecto como ZIP y descomprímelo..

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

1. **Instalar MySQL Workbench** si aún no lo has hecho. [sitio web oficial](https://www.mysql.com/products/workbench/).

2. **Conéctate a tu servidor MySQL**: Abre MySQL Workbench y crea una nueva conexión al servidor MySQL donde deseas alojar tu base de datos. Introduce las credenciales de conexión necesarias.

3. **Crea la base de datos**:
    - Abre un nuevo query tab y ejecuta el siguiente comando SQL para crear tu base de datos:
      ```sql
      CREATE DATABASE nombre_de_tu_base_de_datos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
      ```
    - Asegúrate de reemplazar `nombre_de_tu_base_de_datos` con el nombre que deseas para tu base de datos.
    - Ahora seleccionamos nuestra base de datos creada:
       ```sql
      USE nombre_de_tu_base_de_datos;
      ```

4. **Crea la tabla necesaria**:
    - Ejecuta el siguiente comando SQL para crear la tabla `usuarios` con el formato especificado:
      ```sql
      CREATE TABLE usuarios (
          idusuario INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(100),
          age INT,
          gender CHAR(1)
      );
      ```
      Con esto ya tenemos nuestra tabla creada.

## Configurar variables de entorno en Django

  - **Crear un Archivo `.env`** en el directorio raíz del proyecto con el siguiente contenido:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=nombre_de_usuario
      DATABASE_PASSWORD=contraseña
      DATABASE_HOST=dirección_del_host
      DATABASE_PORT=número_de_puerto 
      ```
      Los valores de `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST` y `DATABASE_PORT` son los que configuraste al crear tu conexión en MySQL Workbench.
      Este es un ejemplo de como debería quedar el archivo `.env` si usas MySQL en local y no has cambiado los valores por defecto:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=root
      DATABASE_PASSWORD=
      DATABASE_HOST=localhost
      DATABASE_PORT=3306
      ```

## Ejecución del proyecto

Con tu entorno configurado y las dependencias instaladas, estás listo para ejecutar el proyecto:

1. **Ejecutar el servidor de desarrollo**:
    - Ejecuta el proyecto con Django parado en la raíz del proyecto:
      ```bash
      python manage.py runserver
      ```
## Uso de la API GraphQL con Postman

- **Para llenar la tabla con registros**:
  Realiza la petición como POST a `http://127.0.0.1:8000/api/fill_table/` indicando el numero de registros que deseas guardar en el body:
```
  {
    "num_entries":"200000"
  }
  ```
**Advertencia**: Cada vez que uses el endpoint para agregar usuarios, la base de datos ejecutará un **TRUNCATE** a la tabla, eliminando todos los registros existentes antes de agregar los nuevos.
- **Para recuperar usuarios**:
  Realiza una consulta en Postman con la petición configurada como GET a `http://127.0.0.1:8000/api/users/` y ya podras ver los resultados en formato JSON y tomar el tiempo de respuesta de la consulta
## Documentación adicional

Esta es la primera parte del proyecto. Accede a la segunda parte para hacer pruebas en graphql: [API GRAPHQL en Django](https://github.com/mframosg/graphql-api).

