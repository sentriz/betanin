FROM node:22-alpine3.23 AS builder-frontend
WORKDIR /src
COPY betanin_client/ .
RUN npm install && \
    npm run build


FROM alpine:3.23 AS builder-mp3gain
WORKDIR /tmp
COPY alpine/mp3gain/APKBUILD .
RUN apk update && \
    apk add --no-cache abuild && \
    abuild-keygen -a -n && \
    cp /root/.abuild/*.pub /etc/apk/keys/ && \
    REPODEST=/tmp/out abuild -F -r


FROM alpine:3.23 AS builder-mp3val
WORKDIR /tmp
COPY alpine/mp3val/APKBUILD .
RUN apk update && \
    apk add --no-cache abuild && \
    abuild-keygen -a -n && \
    cp /root/.abuild/*.pub /etc/apk/keys/ && \
    REPODEST=/tmp/out abuild -F -r


FROM alpine:3.23
LABEL org.opencontainers.image.source=https://github.com/sentriz/betanin
WORKDIR /src
COPY . .
COPY --from=builder-frontend /src/dist/ /src/betanin_client/dist/
COPY --from=builder-mp3gain /tmp/out/*/*.apk /pkgs/
COPY --from=builder-mp3val /tmp/out/*/*.apk /pkgs/

ENV UID=1000
ENV GID=1000
ENV UV_SYSTEM_PYTHON=1
ENV UV_BREAK_SYSTEM_PACKAGES=1
ENV UV_COMPILE_BYTECODE=1

COPY --from=ghcr.io/astral-sh/uv:0.11.2 /uv /usr/local/bin/uv

RUN apk add --no-cache --upgrade --virtual=build-dependencies build-base cmake libffi-dev openssl-dev python3-dev jpeg-dev libpng-dev zlib-dev cargo llvm-dev openblas openblas-dev && \
    apk add --no-cache --upgrade sudo python3 libev chromaprint ffmpeg gstreamer flac keyfinder-cli libsndfile && \
    apk add --no-cache --allow-untrusted /pkgs/* && \
    CFLAGS="-Wno-error=incompatible-pointer-types" uv pip install --no-cache . --requirement requirements-docker.txt && \
    apk del --purge build-dependencies && \
    rm -r /pkgs

VOLUME /b/.local/share/betanin/
VOLUME /b/.config/betanin/
VOLUME /b/.config/beets/

ENV HOME=/b
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

ENTRYPOINT [ "/src/docker-entry" ]
