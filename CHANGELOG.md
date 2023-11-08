# Changelog

### [0.5.5](https://www.github.com/sentriz/betanin/compare/v0.5.4...v0.5.5) (2023-11-08)


### ⚠ BREAKING CHANGES

* **ci:** delete librosa for now

### Features

* **ci:** add debug release action ([f04d4c4](https://www.github.com/sentriz/betanin/commit/f04d4c4ed2f33c8bbe0a440808380c5f00ed0082))


### Bug Fixes

* **ci:** delete librosa for now ([29e3956](https://www.github.com/sentriz/betanin/commit/29e395603bde56083c170f78637df0d94686b8bd))
* **ci:** move docker requirements to txt ([a4a358d](https://www.github.com/sentriz/betanin/commit/a4a358d611cde755fe40b4d4497b533bd79c8de4))
* **ci:** re-enable linux/arm builds ([38721d0](https://www.github.com/sentriz/betanin/commit/38721d04e9975ff2677329868c26da2d299574f2))

### [0.5.4](https://www.github.com/sentriz/betanin/compare/v0.5.3...v0.5.4) (2023-11-07)


### Bug Fixes

* **build:** require flask <3 ([085ca4b](https://www.github.com/sentriz/betanin/commit/085ca4b9ef532cf461b83b167316c960ec8b9e86))
* **ci:** build for linux/amd64 linux/arm64 ([f781037](https://www.github.com/sentriz/betanin/commit/f78103712673d1810d99312947f0071144f3bca4))

### [0.5.3](https://www.github.com/sentriz/betanin/compare/v0.5.2...v0.5.3) (2023-11-07)


### Bug Fixes

* **ci:** only build linux/amd64 for now ([7004071](https://www.github.com/sentriz/betanin/commit/70040715dfdc4d01f6d785c232b50ed6e472a903)), closes [#98](https://www.github.com/sentriz/betanin/issues/98)

### [0.5.2](https://www.github.com/sentriz/betanin/compare/v0.5.1...v0.5.2) (2023-10-18)


### Bug Fixes

* **docker:** add cmake ([fa588cf](https://www.github.com/sentriz/betanin/commit/fa588cf325d5c99c923aa236efeb28c59e3abdfa))

### [0.5.1](https://www.github.com/sentriz/betanin/compare/v0.5.0...v0.5.1) (2023-10-18)


### Bug Fixes

* **docker:** add blas ([#100](https://www.github.com/sentriz/betanin/issues/100)) ([d1c6797](https://www.github.com/sentriz/betanin/commit/d1c67975e4eb2de9654ef300d122e417424ce3a5))

## [0.5.0](https://www.github.com/sentriz/betanin/compare/v0.4.0...v0.5.0) (2023-10-17)


### Features

* **build:** allow custom URL to install beets ([d6e945e](https://www.github.com/sentriz/betanin/commit/d6e945eace0d61e9ac46b89dba4346f35c7017cd))
* **docker:** add beets-bpmanalyser plugin ([#95](https://www.github.com/sentriz/betanin/issues/95)) ([104d394](https://www.github.com/sentriz/betanin/commit/104d394c8871bd5f3a5792c3796d422a3c490bd9))
* **docker:** add beets-lidarr-fields plugin ([#97](https://www.github.com/sentriz/betanin/issues/97)) ([e74bc2f](https://www.github.com/sentriz/betanin/commit/e74bc2f60cc762467f535a0f4271344dbec9a7c5))
* **docker:** add beets-originquery ([1eb6a56](https://www.github.com/sentriz/betanin/commit/1eb6a563f5a6c236309b298aa2746f12d84f7068))
* **docker:** add keyfinder package ([#94](https://www.github.com/sentriz/betanin/issues/94)) ([6153ed8](https://www.github.com/sentriz/betanin/commit/6153ed8843da2132129bd4f852bab0f01a4f18e7))
* **docker:** add support for autobpm plugin ([#98](https://www.github.com/sentriz/betanin/issues/98)) ([4e651fd](https://www.github.com/sentriz/betanin/commit/4e651fd5d67a3511746853d3332548229d1d08aa))


### Bug Fixes

* **ci:** disable pyright ([f1aa8c0](https://www.github.com/sentriz/betanin/commit/f1aa8c0981ca0ec3509c77eb2d60f2a2f09d6388))
* **ci:** fix arm build ([d64200c](https://www.github.com/sentriz/betanin/commit/d64200cbfc37272dee4f1cc2ba9338818c6cb942))
* **docker:** add llvm14-dev to image for librosa build ([22be0ea](https://www.github.com/sentriz/betanin/commit/22be0ea88dadcb54b4e48fe32023fca8c6abef26))
* send to login on 401 ([d2bd050](https://www.github.com/sentriz/betanin/commit/d2bd050d6345e4d9be8c582c77aa904e020b0b00))

## [0.4.0](https://www.github.com/sentriz/betanin/compare/v0.3.41...v0.4.0) (2023-03-31)


### Features

* add `flac` package to docker  image ([84b433e](https://www.github.com/sentriz/betanin/commit/84b433ed2c63762ecfd3ae5554e44150cb4191c2))

### [0.3.41](https://www.github.com/sentriz/betanin/compare/v0.3.39...v0.3.41) (2022-10-05)


### Miscellaneous Chores

* **deps:** bump eventsource from 1.1.0 to 1.1.1 in /betanin_client ([#71](https://www.github.com/sentriz/betanin/issues/71)) ([de5f7b6](https://www.github.com/sentriz/betanin/commit/de5f7b69322d8127cfa16424c06cf20cb2bd43fd))

### [0.3.39](https://www.github.com/sentriz/betanin/compare/v0.3.38...v0.3.39) (2022-09-13)


### Bug Fixes

* sort lines ([427fac2](https://www.github.com/sentriz/betanin/commit/427fac20a36acb8c5d82de4d5fe86a42f02fa65e))

### [0.3.38](https://www.github.com/sentriz/betanin/compare/v0.3.37...v0.3.38) (2022-06-01)


### Bug Fixes

* **ci:** retrigger release-please ([6e27b36](https://www.github.com/sentriz/betanin/commit/6e27b365f841767c044986f62f35890ec63b40f7))

### [0.3.37](https://www.github.com/sentriz/betanin/compare/v0.3.36...v0.3.37) (2022-05-29)


### Bug Fixes

* prune non serialisable fields from apprise details ([61ca4af](https://www.github.com/sentriz/betanin/commit/61ca4af2b2254f359be46440ee181ad3b1fb927d)), closes [#68](https://www.github.com/sentriz/betanin/issues/68)

### [0.3.36](https://www.github.com/sentriz/betanin/compare/v0.3.35...v0.3.36) (2022-05-18)


### Bug Fixes

* log an error if beet not in $PATH ([7c33591](https://www.github.com/sentriz/betanin/commit/7c33591a5ef6bdc29bac8cbc4b59dd4d82a4acaa)), closes [#65](https://www.github.com/sentriz/betanin/issues/65)

### [0.3.35](https://www.github.com/sentriz/betanin/compare/v0.3.34...v0.3.35) (2021-09-22)


### Features

* **image:** add gstreamer for chroma plugin ([#56](https://www.github.com/sentriz/betanin/issues/56)) ([7273c65](https://www.github.com/sentriz/betanin/commit/7273c659a2cd3796d78325b377fbe37ed21f86c1))
* **image:** add opencontainers LABEL ([99638b2](https://www.github.com/sentriz/betanin/commit/99638b2afb2269f364e2eef53d995db176303f23))

### [0.3.34](https://www.github.com/sentriz/betanin/compare/v0.3.33...v0.3.34) (2021-09-22)


### Features

* **image:** add ffmpeg ([4ef84c7](https://www.github.com/sentriz/betanin/commit/4ef84c7b3ecc8fae04717500d46885c43c0c4282)), closes [#54](https://www.github.com/sentriz/betanin/issues/54)


### Bug Fixes

* **image:** chown $HOME at runtime ([ee1d5bf](https://www.github.com/sentriz/betanin/commit/ee1d5bf67cefc50233af2da9fe75b9c922696d4c))

### [0.3.33](https://www.github.com/sentriz/betanin/compare/v0.3.32...v0.3.33) (2021-09-12)


### Bug Fixes

* **ui:** add last read at spacing ([b9cbf6f](https://www.github.com/sentriz/betanin/commit/b9cbf6fb5d8608da0114a3f521918b1a107f547b))

### [0.3.32](https://www.github.com/sentriz/betanin/compare/v0.3.31...v0.3.32) (2021-09-12)


### Bug Fixes

* use SECRET_KEY_PATH when initing secret file ([e55140f](https://www.github.com/sentriz/betanin/commit/e55140fac16c771637bf7a391fff29074c2c7836))

### [0.3.31](https://www.github.com/sentriz/betanin/compare/v0.3.30...v0.3.31) (2021-09-09)


### Features

* support backend pagination ([9bd539a](https://www.github.com/sentriz/betanin/commit/9bd539a129c054cb3a1c79d5c44871296c3ae3b2))


### Bug Fixes

* **ui:** add manual import padding ([a4331c6](https://www.github.com/sentriz/betanin/commit/a4331c65e5d80eeea7939024906b77f63c001153))
* **ui:** add space next to logout button ([bd4250a](https://www.github.com/sentriz/betanin/commit/bd4250a766b1683629dabccaed2712bb689aef3c))
* **ui:** remove overflowing x on small torrents list ([fa7fefa](https://www.github.com/sentriz/betanin/commit/fa7fefaa0ed650879609b8aaaf19a0893eaea076))


### Code Refactoring

* **ui:** clean up binaryInsert ([e644803](https://www.github.com/sentriz/betanin/commit/e64480377ef0abb977282a14390a787c33585e3f))

### [0.3.30](https://www.github.com/sentriz/betanin/compare/v0.3.29...v0.3.30) (2021-09-08)


### Bug Fixes

* start import_torrents before web ([daa8e80](https://www.github.com/sentriz/betanin/commit/daa8e8024d77828dd5ac34fa9867d32756a720e4))

### [0.3.29](https://www.github.com/sentriz/betanin/compare/v0.3.27...v0.3.29) (2021-09-06)


### Bug Fixes

* **docs:** remove old codacy badge ([75704d9](https://www.github.com/sentriz/betanin/commit/75704d995a2001a919a5ad1ea483d9187e091caa))
* move version file to betanin package to that it's installed with site-packages ([8a64998](https://www.github.com/sentriz/betanin/commit/8a649980022095391936d284268cbab8cd7db1d7))

### [0.3.27](https://www.github.com/sentriz/betanin/compare/v0.3.26...v0.3.27) (2021-09-06)


### Features

* **server:** add support for parallel imports ([fc23ad0](https://www.github.com/sentriz/betanin/commit/fc23ad054574fd1ef8cdd57af9e6968f6ff579a7))


### Bug Fixes

* **ci:** install wheel for pypa ([82bb9ea](https://www.github.com/sentriz/betanin/commit/82bb9ea41d8dfc33b84b973c58070d64806cb48b))
* **ui:** don't assume x86_64 for apks ([d832ed7](https://www.github.com/sentriz/betanin/commit/d832ed7579b75841b3d160746131c6c3e2a2a271))

### [0.3.26](https://www.github.com/sentriz/betanin/compare/v1.3.22...v0.3.26) (2021-09-06)


### Features

* **ci:** setup release please ([f7d0493](https://www.github.com/sentriz/betanin/commit/f7d0493a02f1350cff61f6da05044cd93efa73bc))
* **ui:** add prettier check ([4db38ee](https://www.github.com/sentriz/betanin/commit/4db38ee2f7055b11d17950d617d3f4ff9b6e600e))
* **ui:** clean up example scripts ([fd661a4](https://www.github.com/sentriz/betanin/commit/fd661a48413c2221031f7a33a3acd2f9c888e812))
* **ui:** merge two torrents pages ([7d74eaf](https://www.github.com/sentriz/betanin/commit/7d74eaf14b1e68dd8feb2d7c893f3e0c2b5c91c9))
* **ui:** show login error as toast ([c03d81c](https://www.github.com/sentriz/betanin/commit/c03d81cebc54d0d5ff236404dd2f2fa29ea5d02b))


### Bug Fixes

* fix cors for socket connections ([86db374](https://www.github.com/sentriz/betanin/commit/86db374ff7b54801d5377b43a08eaf15cc11e259))
* **ui:** add active state for settings tabs ([964f914](https://www.github.com/sentriz/betanin/commit/964f914af6422ba8feec412ff330605ca933abcf))
* **ui:** don't assume notification service setup url ([c2fa512](https://www.github.com/sentriz/betanin/commit/c2fa512ccdd33e6c99fb01d2a1b3deaeb83c1c98))
* **ui:** update package.json ([3f508fa](https://www.github.com/sentriz/betanin/commit/3f508fa5fe7168b391363a229597657be4dd5802))
* **ui:** use classes ([48fb1b3](https://www.github.com/sentriz/betanin/commit/48fb1b3478027ec3faf525a7d19f52a82b64bd72))
