FROM python:3.6.6-alpine3.6
LABEL maintainer="Senan Kelly <senan@senan.xyz>"
COPY \
    ./requirements-docker.txt \
    ./_docker_entry \
    /
RUN \
    apk add --no-cache libev build-base sudo && \
    pip --no-cache-dir install -U \
        betanin \
        https://github.com/caronc/apprise/archive/master.zip \
        -r /requirements-docker.txt && \
    apk del build-base
VOLUME [ \
    "/root/.local/share/betanin/" \
    "/root/.config/betanin/" \
    "/root/.config/beets/" \
]
ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONWARNINGS="ignore:Unverified HTTPS request" \
    UID=0 \
    GID=0
CMD [ "/_docker_entry" ]
