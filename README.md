# Hud Keys

A client-side Fabric mod that shows the nine hotbar keybinds and their pressed states beside the hotbar.

The current release, **1.0-alpha-1**, adds new features that have not been extensively tested. Please report bugs through [GitHub Issues](https://github.com/hAlex05/Hud-Keys/issues).

## Features

- Hotbar key labels with outlined text and pressed-state feedback.
- Short names for common modifiers and mouse buttons, with automatic text fitting for long labels.
- A brief green flash when attacking and switching hotbar slots within one tick.
- Configurable horizontal/vertical offsets, text scale, and visibility of unpressed keys.
- Settings saved in `config/hudkeys.json`, with an optional Mod Menu configuration screen.

## Supported Minecraft versions

| Minecraft | Java | Release JAR |
| --- | --- | --- |
| 1.21.11 | 21 or newer | `hudk-mc1.21.11-1.0-alpha-1.jar` |
| 26.1, 26.1.1, 26.1.2 | 25 or newer | `hudk-mc26.1.x-1.0-alpha-1.jar` |
| 26.2 | 25 or newer | `hudk-mc26.2-1.0-alpha-1.jar` |
| 26.3 | 25 or newer | `hudk-mc26.3-1.0-alpha-1.jar` |

Use the JAR for your Minecraft version; the 26.1 JAR also supports 26.1.1 and 26.1.2. These are the stable releases from 1.21.11 through 26.3; snapshots and future releases are not covered.

The original Modrinth 26.1 entry was taken down and replaced to fix its embedded compatibility restriction. If you downloaded it, replace it with `hudk-mc26.1.x-1.0-alpha-1.jar` from the current 26.1.x release.

## Installation

1. Install Fabric Loader **0.19.5 or newer** for your Minecraft version.
2. Install [Fabric API](https://modrinth.com/mod/fabric-api) and [Cloth Config](https://modrinth.com/mod/cloth-config), using files compatible with your Minecraft version.
3. Put the matching Hud Keys JAR in your `mods/` folder.
4. Optionally install [Mod Menu](https://modrinth.com/mod/modmenu) to edit settings in-game. Otherwise edit `config/hudkeys.json` while Minecraft is closed.
5. Launch Minecraft using the Fabric profile.

Do not install multiple Hud Keys JARs or a `-sources.jar` file.

## Build from source

Use JDK 25 to build all targets:

```sh
./gradlew build
./gradlew verifyRelease
```

On Windows use `gradlew.bat build`. Each target's JAR is written to `versions/<minecraft-version>/build/libs/`.
To build one target, run `./gradlew :26.3:build` (replace `26.3` as needed).

## Releases and changelog

Downloads: [Modrinth](https://modrinth.com/mod/hud-keys) and [GitHub releases](https://github.com/hAlex05/Hud-Keys/releases).
See [CHANGELOG.md](CHANGELOG.md) for changes compared with 0.1 and 0.1.1.

## Issues and contributions

Report bugs or suggest improvements through [GitHub Issues](https://github.com/hAlex05/Hud-Keys/issues).
Contributions are welcome.

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).
