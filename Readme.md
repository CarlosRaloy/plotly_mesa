# Oxirus System Ticket Analysis

## Instrucciones de Instalacion

1.- Crear un archivo con las variables de entorno

```bash
touch .env
```

```
USER_DB=root
PASSWORD_DB=root
HOST_DB=localhost
DATABASE_DB=My_database
PORT_DB=5432
```

2.- Crear un entorno virtual

Opcion 1
```bash
python -m venv venv
```

Opcion 2
```bash
virtualenv --python=python3 venv && source venv/bin/activate
```

3.- Instalar los requeriments del proyecto

```bash
pip3 install -r requirements.txt
```

4.- Migrar el proyecto
```bash
python3 manage.py migrate
```

```bash
python3 manage.py makemigrations
```

5.- Correr el proyecto 
```bash
python3 manage.py runserver
```

