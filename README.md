# PyArch
Mostly Pythonic Stack

## Docker Quickstart

This app can be run completely using `Docker` and `docker-compose`.

There are three main services:

To run the development version of the notebook and flask app

```bash
docker-compose up pyspark-notebook flask-dev
```

To run the production version of the apps

```bash
docker-compose up pyspark-notebook flask-prod
```

The list of `environment:` variables in the `docker-compose.yml` file takes precedence over any variables specified in `.env`.

To run any commands using the `Flask CLI`

```bash
docker-compose run --rm manage <<COMMAND>>
```

A docker volume `nb_vol` is created to store any Jupyter Notebooks created during dev. Eventually we could look at pointing this at a service like Amazon EBS.
