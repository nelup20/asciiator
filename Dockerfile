
FROM python:3.10.4-slim-bullseye as dev
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root --no-ansi
RUN apt update -y && apt install ffmpeg -y
COPY . .
