FROM python:3.6.6-alpine3.6
LABEL maintainer="Senan Kelly <senan@senan.xyz>"

COPY \
  ./requirements-docker.txt \
  ./_docker_entry \
  /
RUN \
  apk add --no-cache libev build-base libffi-dev sudo && \
  pip --no-cache-dir install -U \
  betanin -r /requirements-docker.txt && \
  apk del build-base
VOLUME /root/.local/share/betanin/
VOLUME /root/.config/betanin/
VOLUME /root/.config/beets/

ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
ENV UID=0
ENV GID=0
CMD [ "/_docker_entry" ]
