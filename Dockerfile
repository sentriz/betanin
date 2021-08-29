FROM node:12.22.1-stretch-slim AS frontend-builder
RUN apt update -qq
RUN apt install -y -qq build-essential python
WORKDIR /src
COPY betanin_client/ .
RUN npm install
RUN PRODUCTION=true npm run-script build


FROM linuxserver/beets
ENV HOME=/root
RUN apk add --no-cache sudo build-base libev libffi-dev openssl-dev python3-dev
WORKDIR /src
COPY . .
COPY --from=frontend-builder /src/dist/ /src/betanin_client/dist/
RUN \
    /usr/bin/pip3 install --no-cache-dir --user . && \
    apk del build-base libffi-dev openssl-dev python3-dev

VOLUME /root/.local/share/betanin/
VOLUME /root/.config/betanin/
VOLUME /root/.config/beets/

ENV UID=0
ENV GID=0
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
ENTRYPOINT [ "/src/docker-entry" ]
