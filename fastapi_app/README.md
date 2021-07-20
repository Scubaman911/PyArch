# fastapi_app

This app can be used as a good base to build microservices from.

### General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.


From `./backend/app/` you can install all the dependencies with:

```console
$ poetry install
```

Then you can start a shell session with the new environment with:

```console
$ poetry shell
```

Next, open your editor at `./fastapi/backend/app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc. Make sure your editor uses the environment you just created with Poetry.

Pydantic schemas in `./fastapi/backend/app/app/schemas/`, API endpoints in `./fastapi/backend/app/app/api/`.

Add and modify tasks to the Celery worker in `./fastapi/backend/app/app/worker.py`.

If you need to install any additional package to the worker, add it to the file `./fastapi/backend/app/celeryworker.dockerfile`.

### Backend tests

#### Test running stack

If your stack is already up and you just want to run the tests, you can use:

```bash
docker-compose exec backend bash /app/tests-start.sh
```

That `/app/tests-start.sh` script just calls `pytest` after making sure that the rest of the stack is running. If you need to pass extra arguments to `pytest`, you can pass them to that command and they will be forwarded.

For example, to stop on first error:

```bash
docker-compose exec backend bash /app/tests-start.sh -x
```

#### Test stack when not running

To test the backend run:

```console
$ DOMAIN=backend sh ./scripts/test.sh
```

The file `./scripts/test.sh` has the commands to generate a testing `docker-stack.yml` file, start the stack and test it.

The tests run with Pytest, modify and add tests to `./backend/app/app/tests/`.


#### Test Coverage

Because the test scripts forward arguments to `pytest`, you can enable test coverage HTML report generation by passing `--cov-report=html`.

To run the tests in a running stack with coverage HTML reports:

```bash
docker-compose exec backend bash /app/tests-start.sh --cov-report=html
```
