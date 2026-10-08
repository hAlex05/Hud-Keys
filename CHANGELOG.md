# Changelog

## 1.0-alpha-1

### Changes since 0.1.1

- Add separate Fabric builds for Minecraft 26.1, 26.1.1, 26.1.2, 26.2, and 26.3, while retaining 1.21.11 support.
- Add a Mod Menu settings screen for horizontal/vertical offsets, text scale, and showing unpressed keys.
- Save settings to `config/hudkeys.json` and recover defaults from missing or invalid configuration files. Invalid text scales reset to 0.6.
- Fit key labels and their outlines inside the hotbar boxes instead of clipping long names to two characters.
- Add compact labels for common modifiers, mouse buttons, and keypad keys.
- Add a brief green flash when attacking and switching slots within one tick; reset flash state when leaving a world.
- Update the HUD integration for newer Minecraft versions, reduce the key-box background opacity, and remove a duplicate background draw.
- Declare exact Minecraft compatibility, Java 21 for 1.21.11 / Java 25 for 26.x, Fabric Loader 0.19.5+, and the required Cloth Config dependency.
- Give each release JAR its Minecraft version in the filename, include the GPL license, and verify all version builds in CI.
- Pin Loom to stable versions, update Gradle for Minecraft 26.3, and update Fabric API, Mod Menu, and Cloth Config dependencies for each target.

### Changes since 0.1

Includes all changes above, plus the long-keybind overflow fix introduced in 0.1.1.

### Installation

Install the JAR matching your exact Minecraft version, Fabric Loader 0.19.5+, Fabric API, and Cloth Config. Mod Menu is optional and provides the in-game settings screen. Minecraft 26.x requires Java 25; 1.21.11 requires Java 21.

This is an alpha release. Support covers the six stable Minecraft versions listed above; future versions and snapshots require separate verification.

## 0.1.1

- Fix long keybind labels overflowing their hotbar boxes by abbreviating labels.
- Minecraft 1.21.11 / Fabric.

## 0.1

- Initial release: display the nine hotbar keybind labels and pressed states with outlined text.
- Minecraft 1.21.11 / Fabric.
