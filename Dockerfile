FROM linuxserver/beets
LABEL maintainer="Senan Kelly <senan@senan.xyz>"

COPY root/ /
COPY ./requirements-docker.txt /
WORKDIR /src
COPY . .
RUN \
 apk add --no-cache \
   build-base \
   libev \
   libffi-dev \
   npm \
   openssl-dev \
   python3-dev \
 && \
 echo "**** install rust ****" && \
 curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
 source $HOME/.cargo/env && \
 cp -R $HOME/.cargo /root/.cargo && \
 echo "**** install betanin ****" && \
 pip --no-cache-dir install -r /requirements-docker.txt && \
 pip --no-cache-dir install -U -e . && \
 echo "**** build frontend ****" && \
 cd betanin_client && \
 npm install && \
 npm update && \
 npm run-script build && \
 echo "**** disable beets web UI ****" && \
 rm -rf /etc/services.d/beets && \
 echo "**** clean up ****" && \
 apk del --purge build-base libffi-dev openssl-dev python3-dev

VOLUME /betanin/data
VOLUME /betanin/config

ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
