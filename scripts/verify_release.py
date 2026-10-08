"""Check the actual distributable JARs before publishing."""

import hashlib
import json
from pathlib import Path
import re
import struct
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def properties(path):
    return dict(
        line.split("=", 1)
        for line in path.read_text().splitlines()
        if "=" in line and not line.lstrip().startswith("#")
    )


def verify():
    version = properties(ROOT / "gradle.properties")["mod_version"]
    settings = (ROOT / "settings.gradle").read_text()
    targets = re.findall(r'"([\d.]+)"', re.search(r"versions (.+)", settings)[1])
    artifacts = []
    for target in targets:
        props = properties(ROOT / "versions" / target / "gradle.properties")
        archive_target = props.get("archive_minecraft_version", target)
        jar = ROOT / "versions" / target / "build/libs" / f"hudk-mc{archive_target}-{version}.jar"
        java = 21 if target.startswith("1.21") else 25
        with zipfile.ZipFile(jar) as archive:
            assert archive.testzip() is None, f"Corrupt JAR: {jar}"
            metadata = json.loads(archive.read("fabric.mod.json"))
            assert metadata["id"] == "hudk"
            assert metadata["version"] == version
            assert metadata["environment"] == "client"
            supported = props.get("supported_minecraft_versions", target).split(",")
            expected = supported if "supported_minecraft_versions" in props else target
            assert metadata["depends"]["minecraft"] == expected
            assert metadata["depends"]["java"] == f">={java}"
            assert metadata["depends"]["fabricloader"] == f'>={props["loader_version"]}'
            assert metadata["depends"]["cloth-config"] == f'>={props["cloth_config_version"]}'
            assert "fabric-api" in metadata["depends"]
            assert "modmenu" in metadata["suggests"]
            assert "modmenu" not in metadata["depends"]
            assert "${" not in json.dumps(metadata), "Unexpanded release metadata"
            assert metadata["icon"] in archive.namelist()
            assert any(name.startswith("LICENSE") for name in archive.namelist())
            for entries in metadata["entrypoints"].values():
                for entry in entries:
                    path = entry.replace(".", "/") + ".class"
                    major = struct.unpack(">H", archive.read(path)[6:8])[0]
                    assert major == java + 44, f"Unexpected bytecode target in {path}"
            artifacts.append({
                "minecraft": target,
                "game_versions": supported,
                "file": str(jar.relative_to(ROOT)),
                "sha512": hashlib.sha512(jar.read_bytes()).hexdigest(),
            })
            print(f"Verified {jar.name}: Minecraft {target}, Java {java}, dependencies and entrypoints")
    # Keep all patch targets as compile checks, but distribute one 26.1-family JAR.
    family_jars = {artifact["minecraft"]: ROOT / artifact["file"] for artifact in artifacts}
    with zipfile.ZipFile(family_jars["26.1"]) as baseline:
        for target in ("26.1.1", "26.1.2"):
            with zipfile.ZipFile(family_jars[target]) as patch:
                for name in baseline.namelist():
                    if name.endswith(".class"):
                        assert baseline.read(name) == patch.read(name), f"26.1-family bytecode differs: {target} {name}"
    artifacts = [a for a in artifacts if a["minecraft"] not in ("26.1.1", "26.1.2")]
    output = ROOT / "build/release-manifest.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"version": version, "artifacts": artifacts}, indent=2) + "\n")
    return artifacts


if __name__ == "__main__":
    verify()
