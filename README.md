<p align="center"><img width="300" src="https://raw.githubusercontent.com/sentriz/betanin/master/betanin_client/src/assets/logo.png"></p>
<h4 align="center">beets based man-in-the-middle of your torrent client and music player</h4>
<p align="center"><a href="http://hub.docker.com/r/sentriz/betanin"><img src="https://img.shields.io/docker/pulls/sentriz/betanin.svg"></a> <a href="https://microbadger.com/images/sentriz/betanin" title="Get your own image badge on microbadger.com"><img src="https://images.microbadger.com/badges/image/sentriz/betanin.svg"></a> <img src="https://api.codacy.com/project/badge/Grade/db7d1db9dd404f8fa31febc8a2d52d00"> <img src="https://img.shields.io/github/issues/sentriz/betanin.svg"> <img src="https://img.shields.io/github/issues-pr/sentriz/betanin.svg"> <img src="https://sentriz.keybase.pub/share/howdy.svg"></p>

<hr>

### installation

    $ pip install --user betanin

<hr>

### usage

    $ betanin [--port=<port>]

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
###### compose
```yml
betanin:
    image: sentriz/betanin
    ports:
    - 9393:9393
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
    "http://betanin:9393/api/torrents"
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
###### working on the backend
there is not much else to do, write your code, `python -m betanin.entry_betanin`, kill it, write your code, etc.
the webserver will be available at *http://localhost:9393/*. the static frontend is served at `/`, and the api is served at `/api`. (there is a swagger ui there too)
also see `python -m betanin.entry_shell`.  
if you need to do a manual migration do `env FLASK_APP='betanin.application:create' flask db migrate --directory betanin_migrations/` (then upgrades are automatically done on betanin start)
###### working on the frontend
start the backend with `python -m betanin.entry_betanin`, but don't use the static frontend served at *http://localhost:9393/*. Instead, in a new shell, do `npm --prefix betanin_client/ run serve` and use the frontend served at *http://localhost:8081/*. it will look for a backend listening on port 9393 locally. after that you can edit anything in `betanin_client/src`, it will be linted and automatically reflected in your web browser.
