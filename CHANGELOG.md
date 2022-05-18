# Changelog

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
