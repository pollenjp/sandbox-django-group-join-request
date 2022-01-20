# template-python-poetry

## Steps

```sh
poetry init
```

```sh
poetry add --dev \
    black \
    flake8 \
    autoflake8 \
    isort \
    mypy \
    nox \
    pytest
```

check your python version and update some config

- `noxfile.py`
  - directory
  - python version
  - `PYTHONPATH`
- `pyproject.toml`
  - mypy's `python_version`

If you use this github template, update `README.md` .
