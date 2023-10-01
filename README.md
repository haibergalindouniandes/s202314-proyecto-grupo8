# Proyecto-202314 

## Equipo Tupperware

## Integrantes:

|   Nombre                         |   Correo                      |
|----------------------------------|-------------------------------|
| Jhon Fredy Guzmán Caicedo        | jf.guzmanc1@uniandes.edu.co   |
| Haiber Humberto Galindo Sanchez  | h.galindos@uniandes.edu.co    |
| Jorge M. Carrillo                | jm.carrillo@uniandes.edu.co   |
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    |

## Documentación del proyecto

La documentación del proyecto correspondiente a la Entrega 3, se encuentra en el siguiente enlace:

[Enlace Onedrive Unidandes](https://uniandes-my.sharepoint.com/:b:/g/personal/s_salazarc_uniandes_edu_co/EZftsFvNlDlBlUIsgv9F1I8BnuF5tW02Ij1bpJF62Dw3tQ?e=ahvNLr)

## Microservicios Implementados

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/7ed6da64-7c3a-42dd-8e22-c2ee86d6bb8a" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/c793bf6b-3fa6-4805-bf85-03102e9eecb0" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/87ab0507-dde2-40c9-8be8-2e313aa688ad" alt="Screenshot" width="500">

## Estructura de las carpetas del Proyecto

### Estructura general de cada microservicio

```
microservice
├── src/ => Carpeta que contiene el código y la lógica necesarios para declarar y ejecutar la API del microservicio.
│	├── main.py => Contiene la configuración base del microservicio.
│	├── blueprints => Contiene la exposición de los recursos ofrecidos por el microservicio.
│	├── commands => Contiene la lógica de las funcionalidades y comunicación con la capa de persistencia.
│	├── errors => Contiene la configuración de los errores que se mostrarán al usuario.
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
│       ├── evaluator_entrega2.yml
│       └── evaluator_entrega3.yml
├── function-sendmail
│   ├── main.py
│   └── requirements.txt
├── nginx
│   └── nginx-proxy.conf
├── rf006
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── query.py
│   │   │   ├── registration.py
│   │   │   ├── reset.py
│   │   │   └── update.py
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
│   ├── .env.database
│   ├── .env.development
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── rf006_poll
│   ├── src
│   │   ├── __init__.py
│   │   └── main.py
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
│   │   │   ├── update.py
│   │   │   └── verify.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── externals
│   │   │   ├── models.py
│   │   │   └── truenative.py
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
├── commands
├── config.yaml
├── docker-compose.yml
├── k8s-componentes-entrega-3.yaml
├── k8s-ingress-deloyment.yaml
├── k8s-true-native-deployment.yaml
├── LICENSE
├── README.md
└── secrets.yml
```

## Pre-requisitos para cada microservicio  
- **Python:** Como lenguaje de programación. Para este proyecto se implementó la versión ```3.10```. Para más información acerca de Python se comparte el siguiente enlace https://www.python.org/.
- **Flask:** Como framework para la creación y despliegue de aplicaciones web de forma sencilla. Para más información acerca de Flask se comparte el siguiente enlace https://flask.palletsprojects.com/en/2.3.x/.
- **pipenv:** Como gestor de entorno virtual del proyecto. Para más información acerca de pipenv se comparte el siguiente enlace https://pipenv.pypa.io/en/latest/.
- **sqlalchemy:** Como ORM (Object Relational Mapper) para la interacción de base de datos. Para más información acerca de sqlalchemy se comparte el siguiente enlace https://www.sqlalchemy.org/.
- **pytest:** Como framework para le construcción y ejecución. Para más información acerca de pytest se comparte el siguiente enlace https://docs.pytest.org/en/7.4.x/.
- **gunicorn:** Como servidor HTTP. Para más información acerca de gunicorn se comparte el siguiente enlace https://gunicorn.org/.
- **PostgreSQL:** Como base de datos relacional para persistir la información. Para más información acerca de PostgreSQL se comparte el siguiente enlace https://www.postgresql.org/.
      
## Pre-requisitos para el despliegue en Local con docker-compose

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

## Despliegue del Proyecto en Local con docker-compose

Para el despliegue del proyecto utilizamos docker-compose que nos permitirá realizar el lanzamiento de cada uno de los contenedores de nuestro proyecto. Para ejecutar docker-compose, utilizamos el siguiente comando:
```bash
docker-compose -f "<RUTA_DEL_ARCHIVO_DOCKER_COMPOSE>" up -d
```
Ejemplo

```bash
docker-compose -f "docker-compose.yml" up -d
```

Una vez se realice el despliegue correspondiente, se debe visualizar en el Docker Desktop lo siguiente:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/6ceabebd-72a1-45d9-b8ba-d2dc4098cd9f" alt="DockerComposeSuccesfull" width="800">

## Pre-requisitos para el despliegue en Google Kubernetes Engine
- **Descargar o clonar el proyecto**: Para ello clonaremos o descargaremos el proyecto del repositorio público, a través del siguiente enlace: https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8.git
- **Crear cuenta de GCP gratis**. Se comparte el siguiente enlace: 
  - [Comenzar gratis](https://cloud.google.com/?utm_source=google&utm_medium=cpc&utm_campaign=latam-CO-all-es-dr-BKWS-all-all-trial-p-dr-1605194-LUAC0014216&utm_content=text-ad-none-any-DEV_c-CRE_512364917207-ADGP_Hybrid+%7C+BKWS+-+PHR+%7C+Txt+~+GCP_General-KWID_43700062788251431-kwd-295915745166&utm_term=KW_gcp-ST_GCP&gclid=Cj0KCQjwjt-oBhDKARIsABVRB0y4CqyDbmLmVJyLke-ozYMuCaxwPaSwMLj6e4CfCTMJNlTq_rWUMtQaAtQyEALw_wcB&gclsrc=aw.ds&hl=es_419)
- **Habilitar el servicio de SQL**: Se comparte el siguiente enlace:
  - [Habilitar servicio](https://cloud.google.com/sql/docs/sqlserver/connect-compute-engine?hl=es-419)
- **Habilitar el servicio de GKE**: Se comparte el siguiente enlace:
  - [Habilitar servicio](https://cloud.google.com/service-usage/docs/enable-disable?hl=es-419)
- **Habilitar el Artifact Registry**: Se comparte el siguiente enlace:
  - [Habilitar servicio](https://console.cloud.google.com/marketplace/product/google/artifactregistry.googleapis.com?hl=es)
- **Habilitar el Cloud Functions**: Se comparte el siguiente enlace:
  - [Habilitar servicio](https://console.cloud.google.com/apis/library/cloudfunctions.googleapis.com?hl=es-EC)

## Despliegue del Proyecto en Google Kubernetes Engine

- Inicialmente se debe realizar la creación del repositorio donde subiremos nuestras imágenes del proyecto, se deben seguir los pasos [Creación repositorio estándar Artifact Registry](https://cloud.google.com/artifact-registry/docs/repositories/create-repos?hl=es-419). 
  
- Posteriormente, debemos autenticarnos a Artifactory Registry con nuestra cuenta de GCP desde una terminal (en este caso Visual Studio Code), ejecutando el siguiente comando que abrirá el navegador web y nos pedirá usuario y contraseña de nuestra cuenta:

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/021a637b-7fd9-4a06-ba94-3b305a4f31e4" alt="Screenshot" width="800">

- Posterior a esto realizamos la construcción de las imágenes de los proyectos. Se debe tener en cuenta que se debe acceder a la carpeta de cada proyecto y ejecutar el siguiente comando:

```bash
docker build -t {region}-docker.pkg.dev/{proyecto}/{artifactory}/users:1.0 --target prod .
```
Ejemplo:

```bash
cd user
docker build -t us-central1-docker.pkg.dev/s202314-proyecto-grupo8/misw-native-microservices-app/users:1.0 --target prod .
```
```bash
cd rf006
docker build -t us-central1-docker.pkg.dev/s202314-proyecto-grupo8/misw-native-microservices-app/rf006:1.0 --target prod .
```
```bash
cd rf006_poll
docker build -t us-central1-docker.pkg.dev/s202314-proyecto-grupo8/misw-native-microservices-app/rf006_poll:1.0 --target prod .
```
Se debe ver en Docker Desktop las imágenes creadas:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/5def689a-d74a-4dba-937b-b944b23f6cc0" alt="Screenshot" width="800">

- Una vez construidas las imágenes, procedemos a subirlas al Artifact Registry. Ejecutamos el siguiente comando:

```bash
docker push {imagen}
```
Ejemplo:

```bash
docker push us-central1-docker.pkg.dev/s202314-proyecto-grupo8/misw-native-microservices-app/users:1.0
```
```bash
docker push us-central1-docker.pkg.dev/s202314-proyecto-grupo8/misw-native-microservices-app/rf006:1.0
```
```bash
docker push us-central1-docker.pkg.dev/s202314-proyecto-grupo8/misw-native-microservices-app/rf006_poll:1.0
```
Se debe ver en Artifact Registry las imágenes:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/2335c27b-fab5-4d9b-828e-56470d29ec51" alt="Screenshot" width="800">

- A continuación, se procede con la creación de la red virtual del proyecto:

```bash
gcloud compute networks create {nombre_red} --project={proyecto} --subnet-mode=custom --mtu=1460 --bgp-routing-mode=regional
```
Ejemplo:

```bash
gcloud compute networks create vpn-s202314-proyecto-grupo8 --project=s202314-proyecto-grupo8 --subnet-mode=custom --mtu=1460 --bgp-routing-mode=regional
```
- Ahora realizamos la creación de la subred correspondiente a los Pods del proyecto:

```bash
gcloud compute networks subnets create {nombre_subred} --range={rango_ips} --network={red_virtual} --region={region} --project={proyecto}
```
Ejemplo:

```bash
gcloud compute networks subnets create red-s202314-proyecto-grupo8 --range=192.168.32.0/19 --network=vpn-s202314-proyecto-grupo8 --region=us-central1 --project=s202314-proyecto-grupo8
```

- Crearemos también la subred correspondiente a la Base de datos que se utilizará en el proyecto:

```bash
gcloud compute addresses create {nombre_db_subred} --global --purpose=VPC_PEERING --addresses=192.168.0.0 --prefix-length=24 --network={red_virtual} --project={proyecto}
```
Ejemplo:

```bash
gcloud compute addresses create red-dbs-s202314-proyecto-grupo8 --global --purpose=VPC_PEERING --addresses=192.168.0.0 --prefix-length=24 --network=vpn-s202314-proyecto-grupo8 --project=s202314-proyecto-grupo8
```

- Procedemos a dar accesos a la red virtual:

```bash
gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --ranges={nombre_db_subred} --network={red_virtual} --project={proyecto}
```
Ejemplo:

```bash
gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --ranges=red-dbs-s202314-proyecto-grupo8 --network=vpn-s202314-proyecto-grupo8 --project=s202314-proyecto-grupo8
```

- Agregamos regla de firewall:

```bash
gcloud compute firewall-rules create allow-db-ingress --direction=INGRESS --priority=1000 --network={red_virtual} --action=ALLOW --rules=tcp:5432 --source-ranges=192.168.1.0/24 --target-tags=basesdedatos --project={proyecto}
```

Ejemplo:

```bash
gcloud compute firewall-rules create allow-db-ingress --direction=INGRESS --priority=1000 --network=vpn-s202314-proyecto-grupo8 --action=ALLOW --rules=tcp:5432 --source-ranges=192.168.1.0/24 --target-tags=basesdedatos --project=s202314-proyecto-grupo8
```

- Una vez teniendo todas las configuraciones anteriores, procederemos a realizar la creación de la base de datos que se utilizará en el proyecto. Para esto seguimos nos dirigimos al servicio **SQL** -> damos clic en **CREAR INSTANCIA** -> damos clic en *Elegir PostgreSQL*:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/36e451dd-3abd-407a-abf7-9dc2637cb50e" alt="Screenshot" width="400">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/aacfd3a3-0d0e-46a1-982f-a8d7501c94b6" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/9897737c-4af8-461c-bf37-7fde174c8566" alt="Screenshot" width="800">

Seguiremos la siguiente configuración para la creación de la BD:

```bash
-> Instancia:
	Nombre: misw-app-nativas-nube-proyecto-grupo8-db
	Contraseña: PgNube202314
	Versión: PostgreSQL 14
	Región: us-central1
	Disponibilidad zonal: Única

-> Maquina y Almacenamiento:
	Tipo de máquina: De núcleo compartido, 1 core y 1.7 GB de RAM
	Almacenamiento 10 GB de HDD
	No habilitar los aumentos automáticos de almacenamiento.

-> Conexiones:
	Asignación de IP de la instancia: privada
	Red: vpn-misw-app-nativas-nube-grupo8
	Rango de IP asignado: red-dbs-misw-app-nativas-nube-proyecto-grupo8
```

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/400dfc82-4b55-419f-b5cf-a7b5bbc76c99" alt="Screenshot" width="800">

Después de unos minutos, debería visualizar la base de datos de la siguiente forma:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/673876d9-a01a-4ccb-9a5b-8820044f8c5d" alt="Screenshot" width="800">

- Desplegamos la Cloud Function para realizar el envió de emails. Ejecutamos desde la terminal el siguiente comando:

```bash
gcloud functions deploy function-send-mail --entry-point hello_http --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region{region} --timeout 60 --min-instances 0 --max-instances 1
```

Ejemplo:

```bash
gcloud functions deploy function-send-mail --entry-point hello_http --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
```

Validamos la función en Cloud Functions

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/99d33208-2fd8-4635-aaa8-828250faafa9" alt="Screenshot" width="800">

- Ahora realizaremos la creación de nuestro Clúster de Kubernentes:

Accedemos al servicio GKE a través del menú de servicio:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/f6c1dbb9-6a11-4a1d-bdc6-e489f107bcb0" alt="Screenshot" width="400">

Damos clic en **CREAR**

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/280a0b3b-830c-4f15-8ab1-2bb61f42d1be" alt="Screenshot" width="800">

Utilizaremos la siguiente configuración:

```bash
Nombre Kubernetes: misw-app-nativas-nube-proyecto-grupo8-k8s
Red: vpn-misw-app-nativas-nube-grupo8
Subred del nodo: red-misw-app-nativas-nube-proyecto-grupo8
Rango de direcciones del pod: 192.168.64.0/21
Rango de direcciones del servicio: 192.168.72.0/21
```
<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/74be42f1-671e-442c-ab68-975b94916bf7" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/2d767952-8f4b-47ed-b803-54c15525717a" alt="Screenshot" width="800">

Una vez se cree el Clúster se debe ver de la siguiente manera:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/5a57f3ec-511c-4892-bc1e-7c6a456fc40d" alt="Screenshot" width="800">

- Antes de lanzar el despliegue de los servicios y el ingress del proyecto, se debe modificar la información del archivo **secrets.yml** cambiando el valor de las variables que están resaltadas en rojo:

Variable **DB_HOST**, la tomamos de la **Dirección IP privada** de nuestra base de datos:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/0324bb6b-6b28-4774-ba4f-765c9c40455c" alt="Screenshot" width="800">

Variable **SEND_EMAIL_PATH**, la tomamos de la **URL del activador** de nuestra función:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/963df511-d330-4787-9461-c0335bb476c1" alt="Screenshot" width="800">

El resultado del archivo **secrets.yml** debe quedar de la siguiente manera:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/dff7e519-b48a-45b4-9373-b377eb2cc70b" alt="Screenshot" width="800">

- Realizamos la implementación de los secrets a través del siguiente comando. Se debe estar en la raíz del proyecto:

```bash
kubectl apply -f secrets.yml
```

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/033c3e24-833f-44b5-8054-494757055271" alt="Screenshot" width="800">

Validamos si la implementación de los secrets fue correcta, siguiendo los siguientes pasos:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/7d64a0c4-95e2-46d2-ad6b-da373ac2a8a0" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/2cbfd9ef-8ab6-4721-8f7f-1f6c78e1f28e" alt="Screenshot" width="800">

- Realizamos el despliegue de TrueNative, a través del siguiente comando:

```bash
kubectl apply -f k8s-true-native-deployment.yaml
```

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/c6fcc620-93d3-457e-ada2-de8dd3a4c0e7" alt="Screenshot" width="800">

- Realizamos el despliegue de los servicios del proyecto, a través del siguiente comando:

```bash
kubectl apply -f k8s-componentes-entrega-3.yaml	
```

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/55bbe5ef-acec-4409-a786-f4b9d2a50548" alt="Screenshot" width="800">

Después de unos minutos, procedemos con la validación en GKE de los Pods y servicios generados:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/fde06332-b1c9-406d-8146-2151a61c31f8" alt="Screenshot" width="800">

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/0c81386d-df28-47d0-b9a3-398acee7b2cd" alt="Screenshot" width="800">

- Por último, realizamos el despliegue del ingress del proyecto, a través del siguiente comando:

```bash
kubectl apply -f k8s-ingress-deloyment.yaml	
```

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/9074cb5d-3fc6-4193-a187-d6663ad3f537" alt="Screenshot" width="800">

Después de unos minutos, procedemos con la validación en GKE del ingress generado:

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/1a9315ca-fbb1-46a8-a2b2-8a2a0ed348d3" alt="Screenshot" width="800">

## Ejecución de Pruebas con Postman

Para probar los servicios API expuestos por cada microservicio, se deben seguir los siguientes pasos:
- Descargar el Collection de Postman en el siguiente enlace [Entrega 3](https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/monitor-202314/main/entrega3/entrega3.json).
- Importar el Collection en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/60091d90-b0da-4c4f-b79e-8f2a2ad6634b" alt="Screenshot" width="800">

- Actualizar la variable **INGRESS_PATH** de la colección.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/05c99636-beb9-4f81-a094-c35bab8ad6aa" alt="Screenshot" width="800">

- Ejecutar el Collection haciendo clic derecho en su nombre y haciendo clic en el botón "Run collection", esto ejecutará múltiples solicitudes API y también ejecutará algunos assertions que hemos preparado para asegurarnos de que el microservicio esté funcionando como se espera.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/75c0feab-9acd-4945-9a95-8e36d2541097" alt="Screenshot" width="800">

## Ejecución del Validador en Github Action Flow

Para la ejecución del validador, que permitirá comprobar que los diferentes microservicios implementados se encuentran de forma correcta y acorde a los diferentes criterios planteados, se deben seguir los siguientes pasos:

- Este evaluador se ejecuta como un workflow de Github Actions en el repositorio. Para ejecutar el workflow, ve a la sección de "Actions" del repositorio que se encuentra en la parte superior.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/68940896-d47e-46a4-9f8e-c4ef4aea2815" alt="Screenshot" width="800">

 - Luego, encontrarás en la sección izquierda una lista de todos los flujos de trabajo (workflows) disponibles para ejecución. En este caso, verás "Evaluator_Entrega1", "Evaluator_Entrega2" y "Evaluator_Entrega3", correspondientes a los evaluadores de las tres entregas. Haz clic en el que deseas ejecutar, para este ejemplo "Evaluator_Entrega3". Verás un botón "Run workflow" en la sección superior derecha, haz clic en este botón, selecciona la rama en la que deseas ejecutarlo y haz clic en el botón "Run workflow".

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/d69fae98-14d9-427f-b022-122a619aa11d" alt="Screenshot" width="800">

- Esto iniciará la ejecución del workflow en la rama. Si todo funciona correctamente y la entrega es correcta, verás que todas las comprobaciones aparecen como aprobadas (passed).

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo8/assets/110913673/32b663cb-a54c-403f-854d-82e4e080a25b" alt="Screenshot" width="800">

