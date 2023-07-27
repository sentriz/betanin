FROM node:16-alpine3.17 AS builder-frontend
WORKDIR /src
COPY betanin_client/ .
RUN npm install && \
    PRODUCTION=true npm run-script build


FROM alpine:3.18 AS builder-mp3gain
WORKDIR /tmp
COPY alpine/mp3gain/APKBUILD .
RUN apk update && \
    apk add --no-cache abuild && \
    abuild-keygen -a -n && \
    REPODEST=/tmp/out abuild -F -r


FROM alpine:3.18 AS builder-mp3val
WORKDIR /tmp
COPY alpine/mp3val/APKBUILD .
RUN apk update && \
    apk add --no-cache abuild && \
    abuild-keygen -a -n && \
    REPODEST=/tmp/out abuild -F -r


FROM alpine:3.18
LABEL org.opencontainers.image.source https://github.com/sentriz/betanin
WORKDIR /src
COPY . .
COPY --from=builder-frontend /src/dist/ /src/betanin_client/dist/
COPY --from=builder-mp3gain /tmp/out/*/*.apk /pkgs/
COPY --from=builder-mp3val /tmp/out/*/*.apk /pkgs/

ENV UID=1000
ENV GID=1000
RUN apk add --no-cache --upgrade --virtual=build-dependencies build-base libffi-dev openssl-dev python3-dev jpeg-dev libpng-dev zlib-dev jpeg-dev && \
    apk add --no-cache --upgrade sudo python3 libev chromaprint ffmpeg gstreamer flac && \
    apk add --no-cache --allow-untrusted /pkgs/* && \
    python3 -m ensurepip && \
    pip3 install --no-cache-dir . --requirement requirements-docker.txt && \
    apk del --purge build-dependencies && \
    rm -r /pkgs ~/.cache

VOLUME /b/.local/share/betanin/
VOLUME /b/.config/betanin/
VOLUME /b/.config/beets/

ENV HOME=/b
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

ENTRYPOINT [ "/src/docker-entry" ]
