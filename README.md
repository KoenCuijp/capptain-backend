# Capptain backend
This repo contains an in-progress Django project: Capptain. The app is meant to help captains of amateur sports teams manage their team. The main usecase is to automatically chase team members to provide their availability for matches and training, as from personal experience I know that's a challenge.

It's a backend API using Django Rest Framework. The frontend (`capptain-frontend` repo) is made with React.

## Tools used
- `poetry` for dependency management
- `ruff`, `black` for linting / format
- `pre-commit` to run linting
- `mypy` for type checking
- `tox` and Github Actions for builds and CI
- `docker` for containization and `docker-compose` to manage multiple containers (1: python container with django, 2: postgres database container)

## running the stack
- Make sure you have the latest version of Docker installed
- Clone the repo
- Run `docker compose up` (older versions of docker: `docker-compose up`, disclaimer: not sure if it's fully compatible with these older versions)
- Run the django migrations in the docker container:
- `docker exec -it capptain-backend poetry run python manage.py makemigrations`
- `docker exec -it capptain-backend poetry run python manage.py migrate`


## Tests

#### Tests package

The package tests themselves are _outside_ of the main library code, in a package that is itself a
Django app (it contains `models`, `settings`, and any other artifacts required to run the tests
(e.g. `urls`).) Where appropriate, this test app may be runnable as a Django project - so that
developers can spin up the test app and see what admin screens look like, test migrations, etc.

#### Running tests

The tests themselves use `pytest` as the test runner. If you have installed the `poetry` evironment,
you can run them thus:

```
$ poetry run pytest
```

or

```
$ poetry shell
(capptain) $ pytest
```

The full suite is controlled by `tox`, which contains a set of environments that will format, lint,
and test against all support Python + Django version combinations.

```
$ tox
...
______________________ summary __________________________
  fmt: commands succeeded
  lint: commands succeeded
  mypy: commands succeeded
  py37-django22: commands succeeded
  py37-django32: commands succeeded
  py37-djangomain: commands succeeded
  py38-django22: commands succeeded
  py38-django32: commands succeeded
  py38-djangomain: commands succeeded
  py39-django22: commands succeeded
  py39-django32: commands succeeded
  py39-djangomain: commands succeeded
```

#### CI

There is a `.github/workflows/tox.yml` file that can be used as a baseline to run all of the tests
on Github. This file runs the oldest (2.2), newest (3.2), and head of the main Django branch.
