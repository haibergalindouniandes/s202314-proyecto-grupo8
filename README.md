# Proyecto-202314 

## Equipo Tupperware

## Integrantes:

|   Nombre                         |   Correo                      |
|----------------------------------|-------------------------------|
| Jhon Fredy Guzmán Caicedo        | jf.guzmanc1@uniandes.edu.co   |
| Haiber Humberto Galindo Sanchez  | h.galindos@uniandes.edu.co    |
| Jorge M. Carrillo                | jm.carrillo@uniandes.edu.co   |
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    |

## Tabla de contenido
- [Estructura de las carpetas del Proyecto](#estructura-de-las-carpetas-del-proyecto)
- [Pre-requisitos para cada microservicio](#pre-requisitos-para-cada-microservicio)
- [Pre-requisitos para el despliegue y pruebas del Proyecto](#pre-requisitos-para-el-despliegue-y-pruebas-del-proyecto)
- [Despliegue del Proyecto](#despliegue-del-proyecto)
- [Ejecución de Pruebas Unitarias y covertura con Pytest](#ejecución-de-pruebas-unitarias-y-covertura-con-pytest)
- [Ejecución de Pruebas con Postman](#ejecución-de-pruebas-con-postman)
- [Ejecución del Validador en Github Action Flow](#ejecución-del-validador-en-github-action-flow)

## Microservicios Implementados

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/2c2f2bbc-9a66-405a-bd1c-959687d0f160" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/a220c4c9-0caf-4678-9493-f39456d24ea2" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/4f56caf0-a6c5-4af1-82f4-b19333b67f2e" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/5e2a21c0-2ab8-4cd5-bcda-84670280bd5a" alt="Screenshot" width="800">

## Estructura de las carpetas del Proyecto

### Estructura general de cada microservicio

```
microservice
├── src/ => Carpeta que contiene el código y la lógica necesarios para declarar y ejecutar la API del microservicio.
│	├── main.py => Contiene la configuración base del microservicio.
│	├── blueprints => Contiene la exposición de los recursos ofrecidos por el microservicio.
│	├── commands => Contiene la lógica de las funcionalidades y comunicación con la capa de persistencia.
│	├── errors => Contiene la configuración de lo errores que se mostrarán al usuario.
│	├── models => Contiene la configuración de los modelos que se utilizarán para la creación de las tablas en la base de datos.
│	├── utilities => Contiene las funcionalidades utilitarias del servicio.
│	└── validators => Contiene las funcionalidades que validan diferentes procesos del servicio.
└── tests/ => Carpeta que contiene las pruebas para los componentes principales del microservicio que han sido declarados en la carpeta `/src`.
	├── conftest.py => Contiene la configuración base de las pruebas.
	├── blueprints => Contiene las pruebas enfocadas en la capa de exposición del servicio.
	└── commands => Contiene las pruebas enfocadas en la capa lógica del servicio.
```

### Estructura completa del proyecto

```
.
├── .github
│   └── workflows
│       ├── ci_pipeline.yml
│       ├── evaluator_entrega1.yml
│       └── evaluator_entrega2.yml
├── _old
│   └── README.md
├── offers
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── list.py
│   │   │   └── reset.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── utilities
│   │   │   ├── __init__.py
│   │   │   └── utilities.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── test
│   │   ├── blueprints
│   │   │   └── test_resources.py
│   │   ├── commands
│   │   │   ├── test_create.py
│   │   │   ├── test_delete.py
│   │   │   ├── test_get.py
│   │   │   └── test_list.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.template
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── posts
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   └── vistas.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── query.py
│   │   │   └── reset.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── config.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   └── main.py
│   ├── test
│   │   ├── commands
│   │   │   ├── test_create.py
│   │   │   ├── test_delete.py
│   │   │   ├── test_get.py
│   │   │   └── test_query.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── routes
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── query.py
│   │   │   ├── reset.py
│   │   │   └── update.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── queries
│   │   │   ├── __init__.py
│   │   │   ├── base_query.py
│   │   │   └── detail.py
│   │   ├── utilities
│   │   │   ├── __init__.py
│   │   │   └── utilities.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── test
│   │   ├── blueprints
│   │   │   └── test_resources.py
│   │   ├── commands
│   │   │   ├── test_create.py
│   │   │   ├── test_delete.py
│   │   │   ├── test_get.py
│   │   │   └── test_query.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.template
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── users
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── authenticate.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── reset.py
│   │   │   └── update.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── queries
│   │   │   ├── __init__.py
│   │   │   ├── base_query.py
│   │   │   └── detail.py
│   │   ├── utilities
│   │   │   ├── __init__.py
│   │   │   └── utilities.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── test
│   │   ├── blueprints
│   │   │   └── test_resources.py
│   │   ├── commands
│   │   │   ├── test_authenticate.py
│   │   │   ├── test_create.py
│   │   │   └── test_update.py
│   │   ├── commands
│   │   │   └── test_detail.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── .gitignore
├── LICENSE
├── README.md
├── config.yaml
└── docker-compose.yml
```

## Pre-requisitos para cada microservicio  
- **Python:** Como lenguaje de programación. Para este proyecto se implemento la versión ```3.10```. Para más información acerca de Python se comparte el siguiente enlace https://www.python.org/.
- **Flask:** Como framework para la creación y despliegue de aplicaciones web de forma sencilla. Para más información acerca de Flask se comparte el siguiente enlace https://flask.palletsprojects.com/en/2.3.x/.
- **pipenv:** Como gestor de entorno virtual del proyecto. Para más información acerca de pipenv se comparte el siguiente enlace https://pipenv.pypa.io/en/latest/.
- **sqlalchemy:** Como ORM (Object Relational Mapper) para la interacción de base de datos. Para más información acerca de sqlalchemy se comparte el siguiente enlace https://www.sqlalchemy.org/.
- **pytest:** Como framework para le construcción y ejecución. Para más información acerca de pytest se comparte el siguiente enlace https://docs.pytest.org/en/7.4.x/.
- **gunicorn:** Como servidor HTTP. Para más información acerca de gunicorn se comparte el siguiente enlace https://gunicorn.org/.
- **PostgreSQL:** Como base de datos relacional para persistir la información. Para más información acerca de PostgreSQL se comparte el siguiente enlace https://www.postgresql.org/.
      
## Pre-requisitos para el despliegue y pruebas del Proyecto

### Docker:
- En primera instancia se debe tener instalado **Docker**. Para esto se comparten los siguientes enlaces:
  - **Instalación de docker en Windows**: https://docs.docker.com/desktop/install/windows-install
  - **Instalación de docker en Linux Ubuntu**: https://docs.docker.com/engine/install/ubuntu
  - **Instalación de docker en Mac**: https://docs.docker.com/desktop/install/mac-install/.

### Postman:

- Para realizar las pruebas del servicio, se debe instalar **Postman**.Para esto se comparten los siguientes enlaces:
  - **Instalación de docker en Windows**: https://learning.postman.com/docs/getting-started/installation/installation-and-updates/#installing-postman-on-windows
  - **Instalación de docker en Linux Ubuntu**: https://learning.postman.com/docs/getting-started/installation/installation-and-updates/#installing-postman-on-linux
  - **Instalación de docker en Mac**: https://learning.postman.com/docs/getting-started/installation/installation-and-updates/#installing-postman-on-mac

## Despliegue del Proyecto

Para el despliegue del proyecto utilizamos docker-compose que nos permitirá realizar el lanzamiento de cada uno de los contenedores de nuestro proyecto. Para ejecutar docker-compose, utilizamos el siguiente comando:
```bash
$> docker-compose -f "<RUTA_DEL_ARCHIVO_DOCKER_COMPOSE>" up -d

# Ejemplo
$> docker-compose -f "docker-compose.yml" up -d
```

Una vez se realice el despliegue correspondiente, se debe visualizar en el Docker Desktop lo siguiente:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/0d92fb6d-7926-4843-b7a5-aa6419214e7c" alt="DockerComposeSuccesfull" width="800">

## Ejecución de Pruebas Unitarias y covertura con Pytest

Para ejecutar las pruebas unitarias de los microservicios y establecer el porcentaje mínimo de cobertura del conjunto de pruebas en 70%, se debe ingresar a la carpeta del microservicio al que se le desea realizar las pruebas y lanzar el comando de pytest de la siguiente manera:

```bash
$> cd carpeta/
$> pytest --cov-fail-under=70 --cov=src

# Ejemplo
$> cd users/
$> pytest --cov-fail-under=70 --cov=src
```

El resultado obtenido deber muy parecido a:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/7b99ccf4-77b5-4bb7-8b47-3b55a2d9c1eb" alt="DockerComposeSuccesfull" width="800">

Si se desea realizar las pruebas pero que nos genere un reporte en HTML con el resultado obtenido, se debe ejecutar el siguiente comando:

```bash
$> cd carpeta/
$> pytest --cov-fail-under=70 --cov=src --cov-report=html

# Ejemplo
$> cd users/
$> pytest --cov-fail-under=70 --cov=src --cov-report=html
```

## Ejecución de Pruebas con Postman

Para probar los servicios API expuestos por cada microservicio, se deben seguir los siguientes pasos:
- Descargar el Collection de Postman en el siguiente enlace [Entrega 1](https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/monitor-202314/main/entrega1/entrega1.json).
- Impórtar el Collection en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/836f6199-9343-447a-9bce-23d8c07d0338" alt="Screenshot" width="800">

- Actualizar las variables de colección que especifican la URL donde se está ejecutando cada microservicio.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/efafbb3d-5938-4bd8-bfc7-6becfccd2682" alt="Screenshot" width="800">

- Ejecutar el Collection haciendo clic derecho en su nombre y haciendo clic en el botón "Run collection", esto ejecutará múltiples solicitudes API y también ejecutará algunos assertions que hemos preparado para asegurarnos de que el microservicio esté funcionando como se espera.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/f5ca6f7c-e4f4-4209-a949-dcf3a6dab9e3" alt="Screenshot" width="800">

## Ejecución del Validador en Github Action Flow

Para la ejecución del validador, que permitirá comprobar que los diferentes microservicios implementados se encuentran de forma correcta y acorde a los diferentes criterios planteados, se deben seguir los siguientes pasos:

- Este evaluador se ejecuta como un workflow de Github Actions en el repositorio. Para ejecutar el workflow, ve a la sección de "Actions" del repositorio que se encuentra en la parte superior.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/92d686b7-21b1-42b1-b23a-e8c3d626dfd3" alt="Screenshot" width="800">

 - Luego, encontrarás en la sección izquierda una lista de todos los flujos de trabajo (workflows) disponibles para ejecución. En este caso, verás "Evaluator_Entrega1" y "Evaluator_Entrega2", correspondientes a los evaluadores de las dos primeras entregas. Haz clic en el que deseas ejecutar. Verás un botón "Run workflow" en la sección superior derecha, haz clic en este botón, selecciona la rama en la que deseas ejecutarlo y haz clic en el botón "Run workflow".

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/4bcf1c0d-e422-4f9d-9ff6-a663f8248352" alt="Screenshot" width="800">

- Esto iniciará la ejecución del workflow en la rama. Si todo funciona correctamente y la entrega es correcta, verás que todas las comprobaciones aparecen como aprobadas (passed).

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202314-base/assets/78829363/c6c580b2-80e0-411d-8971-a252312ce5ea" alt="Screenshot" width="800">
