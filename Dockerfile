
FROM python:3.10.4-slim-bullseye as dev
WORKDIR /app
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-root
# TODO: why doesn't Poetry install Pillow?
RUN pip install Pillow
RUN apt update -y
RUN apt install ffmpeg -y
COPY . .
