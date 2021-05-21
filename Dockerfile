FROM linuxserver/beets
LABEL maintainer="Senan Kelly <senan@senan.xyz>"

COPY root/ ./requirements-docker.txt /
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
 echo "**** install betanin ****" && \
 pip3 --no-cache-dir install -r /requirements-docker.txt && \
 pip3 --no-cache-dir install -U -e . && \
 echo "**** install latest beets version (workaround for https://github.com/linuxserver/docker-beets/issues/80) ****" && \
 pip3 install -q --no-cache-dir https://github.com/beetbox/beets/zipball/master && \
 echo "**** build frontend ****" && \
 cd betanin_client && \
 npm install && \
 npm update && \
 npm run-script build && \
 echo "**** disable beets web UI ****" && \
 rm -rf /etc/services.d/beets && \
 echo "**** add UID/GID env support ****" && \
 sed -i 's/PUID=${PUID:-911}/PUID=${PUID:-${UID:-911}}/g' /etc/cont-init.d/10-adduser && \
 sed -i 's/PGID=${PGID:-911}/PGID=${PGID:-${GID:-911}}/g' /etc/cont-init.d/10-adduser && \
 echo "**** clean up ****" && \
 rustup self uninstall -y && \
 apk del --purge build-base libffi-dev openssl-dev python3-dev

VOLUME ["/betanin/data", "/betanin/config"]

ENV PYTHONUNBUFFERED=1 \
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

CMD ["/_docker_entry"]