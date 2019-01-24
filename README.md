<p align="center"><img width="300" src="https://github.com/sentriz/betanin/blob/master/betanin/client/src/assets/logo.png?raw=true"></p>
<h4 align="center">beets based man-in-the-middle of your torrent client and music player</h4>
<p align="center"><a href="http://hub.docker.com/r/sentriz/betanin"><img src="https://img.shields.io/docker/pulls/sentriz/betanin.svg"></a> <img src="https://api.codacy.com/project/badge/Grade/db7d1db9dd404f8fa31febc8a2d52d00"> <img src="https://img.shields.io/github/issues/sentriz/betanin.svg"> <img src="https://img.shields.io/github/issues-pr/sentriz/betanin.svg"> <img src="https://img.shields.io/badge/python-3.6-blue.svg"> <img src="https://img.shields.io/badge/vue-2.5-brightgreen.svg"></p>

<hr>

### installation

    pip install --user requirements.txt
    pip install git+https://github.com/edavis/transmission-fluid
    ./wrap-client install           # todo: host the compiled frontend somewhere
    ./wrap-client run-script build  # ^^^^
    ./create-database

<hr>

### usage
    ./start
    
<hr>

### docker
###### image
`docker pull sentriz/betanin`  
###### volumes
`/root/.local/share/betanin/` for a persistent database  
`/root/.config/betanin/` for a persistent betanin config  
`/root/.config/beets/` for a persistent beets home (point this to your current beets home if you have one)  
`/music/` so beets can access your music  
`/downloads/` so beets can access your downloads  
###### port
5000
###### compose (example with [traefik](https://traefik.io/))
```yml
betanin:
    container_name: betanin
    image: sentriz/betanin
    labels:
      traefik.docker.network: <your external network>
      traefik.frontend.auth.basic: ${HTPASSWD}
      traefik.frontend.rule: Host:betanin.${DOMAIN}
    networks:
    - proxy
    restart: unless-stopped
    volumes:
    - ${DATA}/betanin/data:/root/.local/share/betanin/
    - ${DATA}/betanin/config:/root/.config/betanin/
    - ${DATA}/betanin/beets:/root/.config/beets/
    - ${MEDIA}/music:/music/
    - ${MEDIA}/downloads:/downloads/
```

<hr>

### transmission
###### settings.json (example excerpt)
```json
...
"script-torrent-done-enabled": true,
"script-torrent-done-filename": "/scripts/done",
...
```
###### done script
```bash
#!/bin/sh


curl \
    --request POST \
    --data-urlencode "path=/downloads/complete/beets" \
    --data-urlencode "name=$TR_TORRENT_NAME" \
    --user 'user:password' \
    "http://betanin:5000/api/torrents/$TR_TORRENT_HASH"
```
###### docker compose (excerpt)
```yaml
volumes:
- ${DATA}/transmission/config:/config
- ${DATA}/transmission/scripts:/scripts
- ${MEDIA}/download:/downloads
```

<hr>

### developing
make sure you have installed betanin (see above)
###### working on the backend
there is not much else to do, write your code, `/start`, kill it, write your code, etc.
the webserver will be available at *http://localhost:5000/*. the static frontend is served at `/`, and the api is served at `/api`. (there is a swagger ui there too)
###### working on the frontend
start the backend with `./start`, but don't use the static frontend served at *http://localhost:5000/*. Instead, in a new shell, do `./wrap-client run server` and use the frontend served at *http://localhost:8081/*. it will look for a backend listening on port 5000 locally. after that you can edit anything in `betanin/client/src`, it will be linted and automatically reflected in your web browser.
###### testing / emulation
there is a script to mock a transmission webhook at [scripts/mock_transmission_done](https://github.com/sentriz/betanin/blob/master/scripts/mock_transmission_done), and other scripts that try to mock beets itself in [scripts/](https://github.com/sentriz/betanin/blob/master/scripts/). which should be changed [here](https://github.com/sentriz/betanin/blob/master/betanin/api/jobs/import_torrents.py).
