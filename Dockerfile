FROM python:3.8-slim-bookworm


COPY src pyproject.toml /src/

WORKDIR /src
RUN pip install .

WORKDIR /app

CMD [ "gmp-sync-targets" ]
