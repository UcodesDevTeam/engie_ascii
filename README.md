# ENGIE

Base project for engie interview.

## For Production
### Installation
```shell
pip install -e .
```

### Running
```shell
uvicorn wsgi:app
```

## For Development
### Installation
```shell
pip install -e ".[dev]"
pre-commit install
```
### Running the application
```shell
flask run
```

### Running tests
```shell
pytest
```

### Pre Commit
The pre-commit scripts can be manually executed with `pre-commit run --all-files`.
