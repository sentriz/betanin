<p align="center">
  <img width="300" src="https://github.com/sentriz/betanin/blob/master/betanin/client/src/assets/logo.png?raw=true">
</p>
<h4 align="center">beets based man-in-the-middle of your torrent client and music player</h4>
<h2 align="center">this project is not finished yet</h2>

### todo
  - [x] not do that thing in `torrent_client`
  - [x] socket stuff
  - [x] only add the torrent's ID to the process queue
  - [x] start beets stuff
  - [x] console in vuex
  - [x] stdin streaming
  - [x] support multiple remotes
  - [ ] vuex modules
  - [ ] start sheduler based on if flask command was `run`
  - [x] host testing
  - [ ] fix toast position
  - [ ] pluggable `beets`
  - [ ] generic plugin config editor
  - [ ] "input needed" regex matching stdout
  - [ ] generic "expect" line to vue buttons config
  
### 🔥🔥🔥 hot tech used 🔥🔥🔥
  - vue
  - vuex
  - vue router
  - webpack
  - pug
  - scss
  - buefy
  - bulma
  - axios
  - flask
  - socketio
  - albemic
  - sqlalchemy
  - sqlite3

### installation

    pip install --user requirements.txt
    pip install git+https://github.com/edavis/transmission-fluid

### docker
`docker pull sentriz/betanin`  
more docs to come, but for now, mount these volumes  
`/root/.local/share/betanin/` for a persistent database  
`/root/.config/beets/` for a persistent beets home (point this to your current beets home if you have one)  
`/music` so beets can access your music  
compose
```
betanin:
  container_name: betanin
  image: sentriz/betanin
  labels:
    traefik.docker.network: proxy
    traefik.enable: 'true'
    traefik.frontend.auth.basic: ${HTPASSWD}
    traefik.frontend.rule: Host:betanin.${DOMAIN}
  networks:
  - proxy
  restart: unless-stopped
  volumes:
  - ${DATA}/betanin/data:/root/.local/share/betanin/
  - ${DATA}/betanin/beets:/root/.config/beets/
  - ${MEDIA}/music:/music/
```
