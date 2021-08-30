FROM node:12.22.1-stretch-slim AS frontend-builder
RUN apt-get update -qq && \
    apt-get install -y -qq --no-install-recommends build-essential python
WORKDIR /src
COPY betanin_client/ .
RUN npm install && \
    PRODUCTION=true npm run-script build


FROM alpine:3.14.2 AS mp3gain-builder
WORKDIR /tmp
COPY alpine/mp3gain/APKBUILD .
RUN apk update && \
    apk add --no-cache abuild && \
    abuild-keygen -a -n && \
    REPODEST=/tmp/out abuild -F -r


FROM alpine:3.14.2 AS mp3val-builder
WORKDIR /tmp
COPY alpine/mp3val/APKBUILD .
RUN apk update && \
    apk add --no-cache abuild && \
    abuild-keygen -a -n && \
    REPODEST=/tmp/out abuild -F -r


FROM alpine:3.14.2

RUN apk add --no-cache sudo build-base libffi-dev openssl-dev python3-dev jpeg-dev libpng-dev zlib-dev jpeg-dev libev chromaprint

COPY --from=mp3gain-builder /tmp/out/x86_64/*.apk /pkgs/
COPY --from=mp3val-builder /tmp/out/x86_64/*.apk /pkgs/
RUN apk add --no-cache --allow-untrusted /pkgs/* && \
    rm -r /pkgs

ENV UID=1000
ENV GID=1000
RUN adduser -D -h /b -u "$UID" -g "$GID" betanin

WORKDIR /src
COPY . .
COPY --from=frontend-builder /src/dist/ /src/betanin_client/dist/
RUN python3 -m ensurepip && \
    pip3 install --no-cache-dir . --requirement requirements-docker.txt && \
    apk del build-base libffi-dev openssl-dev python3-dev jpeg-dev libpng-dev zlib-dev jpeg-dev

VOLUME /b/.local/share/betanin/
VOLUME /b/.config/betanin/
VOLUME /b/.config/beets/

ENV HOME=/b
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
ENTRYPOINT [ "/src/docker-entry" ]
