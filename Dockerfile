FROM python:3.11-alpine

# Make sure we have poetry to install dependencies
RUN pip install poetry --upgrade --progress-bar off

# Make sure the output of python is being logged in the terminal in realtime
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/capptain-backend

# # Copy the depencency files for poetry to install
# COPY pyproject.toml poetry.lock poetry.toml ./

# # Poetry requires a readme, but it doesn't make sense 
# # to copy the github repo readme into the container
# RUN touch README.md

# Copy project file
COPY pyproject.toml .

# Install the dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy the django app code for capptain
COPY . .

# Make sure there's no virtual env, we don't need it in a container
RUN rm -rf .venv

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]