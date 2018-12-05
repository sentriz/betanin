FROM node:8 as frontend-builder
WORKDIR /app
COPY betanin/client/package*.json ./
COPY betanin/client/vue.config.js ./
COPY betanin/client/src/ ./src/
COPY betanin/client/public/ ./public/
ARG SOURCE_COMMIT
RUN \
    npm install && \
    npm run-script build

FROM python:3.6.6-alpine3.6
LABEL maintainer="Senan Kelly <senan@senan.xyz>"
WORKDIR /app
COPY requirements.txt start create-database docker-entry ./
COPY betanin/*.py ./betanin/
COPY betanin/api/ ./betanin/api
COPY betanin/client/__init__.py ./betanin/client/
COPY --from=frontend-builder /app/dist/ ./betanin/client/dist
RUN \
    apk add --no-cache libev python3-dev build-base git && \
    pip install \
        -r requirements.txt \
        beets \
        git+https://github.com/edavis/transmission-fluid \
        discogs-client \
        beets-noimport
VOLUME /root/.local/share/betanin/
VOLUME /root/.config/betanin/
VOLUME /root/.config/beets/
EXPOSE 5000
CMD [ "./docker-entry" ]
