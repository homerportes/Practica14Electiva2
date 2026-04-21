# Practica 13: Ciclo completo DevOps

Esta practica contiene una aplicacion web "Hola Mundo" hecha en Python, lista para ejecutarse con Docker y automatizada con GitHub Actions.

## 1. Ejecutar la app localmente

```bash
python app.py
```

Abrir en el navegador:

```text
http://localhost:8000
```

## 2. Crear la imagen Docker

Imagen usada en esta practica:

```text
oxpo26/practica13-hola-mundo
```

```bash
docker build -t oxpo26/practica13-hola-mundo:1.0 .
```

## 3. Ejecutar el contenedor

```bash
docker run --rm -p 8000:8000 oxpo26/practica13-hola-mundo:1.0
```

Abrir:

```text
http://localhost:8000
```

## 4. Iniciar sesion en Docker Hub

```bash
docker login
```

## 5. Subir la imagen a Docker Hub

```bash
docker push oxpo26/practica13-hola-mundo:1.0
```

## 6. Automatizacion con GitHub Actions

El archivo del workflow esta en:

```text
.github/workflows/deploy.yml
```

Este workflow se ejecuta al hacer push a la rama `main` y realiza lo siguiente:

1. Descarga el codigo del repositorio.
2. Inicia sesion en Docker Hub.
3. Construye la imagen Docker.
4. Sube la imagen a Docker Hub con tres tags:
   - `latest`
   - SHA corto del commit
   - fecha del build
5. Dispara el deploy automatico en Render usando su API.

## 7. Secrets necesarios en GitHub

En el repositorio de GitHub, ir a:

```text
Settings > Secrets and variables > Actions > New repository secret
```

Crear estos secrets:

| Secret | Valor |
| --- | --- |
| `DOCKER_USERNAME` | `oxpo26` |
| `DOCKERHUB_TOKEN` | Access Token de Docker Hub |
| `RENDER_API_KEY` | API Key de Render |
| `RENDER_SERVICE_ID` | ID del servicio en Render, por ejemplo `srv-xxxxxxxxxxxx` |

## 8. Crear Access Token de Docker Hub

1. Entrar a Docker Hub.
2. Ir a Account Settings > Security.
3. Crear un nuevo Access Token.
4. Copiar el token y guardarlo en GitHub como `DOCKERHUB_TOKEN`.

## 9. Configurar Render

1. Crear un Web Service en Render.
2. Conectarlo al repositorio de GitHub o configurarlo para usar la imagen:

```text
oxpo26/practica13-hola-mundo:latest
```

3. Copiar el Service ID desde la URL del servicio. Ejemplo:

```text
https://dashboard.render.com/web/srv-xxxxxxxxxxxx
```

4. Crear una API Key en Render y guardarla en GitHub como `RENDER_API_KEY`.

Cuando hagas push a `main`, GitHub Actions subira la imagen a Docker Hub y activara el deploy en Render.

## Archivos incluidos

- `app.py`: aplicacion web Hola Mundo.
- `Dockerfile`: instrucciones para construir la imagen.
- `.dockerignore`: archivos que Docker debe ignorar al construir la imagen.
- `.github/workflows/deploy.yml`: automatizacion CI/CD con Docker Hub y Render.
