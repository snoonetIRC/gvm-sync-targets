FROM python:3.8-slim-bookworm


COPY ./src/ /src/src
COPY pyproject.toml README.md /src/

WORKDIR /src
RUN pip install .

WORKDIR /app

CMD [ "gmp-sync-targets" ]
