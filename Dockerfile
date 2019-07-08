FROM python:3.6.6-alpine3.6
LABEL maintainer="Senan Kelly <senan@senan.xyz>"
COPY ./requirements-docker.txt /
RUN \
    apk add --no-cache libev build-base && \
    pip --no-cache-dir install -U \
        betanin \
        https://github.com/caronc/apprise/archive/master.zip \
        -r /requirements-docker.txt && \
    apk del build-base
VOLUME /root/.local/share/betanin/
VOLUME /root/.config/betanin/
VOLUME /root/.config/beets/
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
CMD [ "betanin" ]
