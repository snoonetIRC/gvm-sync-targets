FROM python:3.9 AS builder

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
    pipx && \
    apt-get remove --purge --auto-remove -y && \
    rm -rf /var/lib/apt/lists/*

RUN pipx install hatch

COPY . /source
WORKDIR /source

RUN rm -rf dist && /root/.local/bin/hatch build -t wheel

FROM python:3.9-slim

WORKDIR /gvm-sync-targets

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
    gosu && \
    apt-get remove --purge --auto-remove -y && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --gid 1001 --system gvm && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group gvm

COPY --from=builder /source/dist/* /gvm-sync-targets/
COPY .docker/entrypoint.sh /usr/local/bin/entrypoint

RUN python3 -m pip install --break-system-packages /gvm-sync-targets/*

RUN chown -R gvm:gvm /gvm-sync-targets && \
    chmod 755 /usr/local/bin/entrypoint

ENTRYPOINT [ "/usr/local/bin/entrypoint" ]

CMD [ "gvm-sync-targets" ]
