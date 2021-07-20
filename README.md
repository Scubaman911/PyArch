# PyArch
Mostly Pythonic Stack

## Project Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.


## Stack overview

* Start the stack with Docker Compose:

```bash
docker-compose up
```

* Now you can open your browser and interact with these URLs:

Backend microservice, JSON based web API based on OpenAPI: http://localhost/api/

JupyterLab, web-based interface for interacting with Jupyter: http://localhost:8008/lab

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost/redoc

Flower, administration of Celery tasks: http://localhost:5555

Traefik UI, to see how the routes are being handled by the proxy: http://localhost:8090


If your Docker is not running in `localhost` (the URLs above wouldn't work) check the sections below on **Development with Docker Toolbox** and **Development with a custom IP**.

