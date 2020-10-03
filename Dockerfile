FROM linuxserver/beets:nightly
LABEL maintainer="Senan Kelly <senan@senan.xyz>"

COPY /root /

RUN apk add --no-cache --virtual=build-deps --upgrade \
        libev \
        build-base \
        libffi-dev \
        git \
        python3-dev

# Remove problematic dependency
RUN pip3 uninstall -y enum34

# Install Betanin
RUN pip3 install -U \
    betanin \
    https://github.com/caronc/apprise/archive/master.zip \
    https://github.com/beetbox/beets/archive/master.zip

# Disable Beets web UI
RUN rm -rf /etc/services.d/beets

# Clean up
RUN apk del --purge \
        build-deps
RUN rm -rf /tmp/*

VOLUME \
    "/config/.config/beets" \
    "/config/.config/betanin" \
    "/config/.local/share/betanin" \
    "/downloads" \
    "/music"
