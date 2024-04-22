# Prueba GES

## Descripción

Este proyecto es una prueba para el proceso de selección de GES.

## Requerimientos

Crear un nuevo etorno virtual a elección con Python 3.10

- Python 3.10

## Instalación

Para instalar las dependencias del proyecto, ejecutar el siguiente comando:

```bash
pip install -r requirements.txt \
&& python manage.py makemigrations && python manage.py migrate \
&& python manage.py loaddata fixtures/users.json
&& python manage.py loaddata fixtures/students.json
```

## Ejecución

Para ejecutar el proyecto, ejecutar el siguiente comando:

```bash
python manage.py runserver 8000
```

## Edpoints

Una vez ejecutado el proyecto, puedes acceder a la documentación de swagger en la siguiente URL:

- http://127.0.0.1:8000/api/v1/docs/

## Usuarios

El proyecto cuenta con un sistema de autenticación basado en JWT, para acceder a los endpoints es necesario autenticarse.:

### Administrador
- Usuario: ges_admin
- Contraseña: Ges$2024
