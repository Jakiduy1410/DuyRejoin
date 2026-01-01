import subprocess
import json

CONFIG = "config/config.json"


def load_config():
    with open(CONFIG) as f:
        return json.load(f)


def save_config(cfg):
    with open(CONFIG, "w") as f:
        json.dump(cfg, f, indent=2)


def get_packages_by_prefix():
    cfg = load_config()
    prefix = cfg["package_prefix"]

    out = subprocess.getoutput("pm list packages")
    pkgs = []

    for line in out.splitlines():
        pkg = line.replace("package:", "")
        if f".{prefix}" in pkg:
            pkgs.append(pkg)

    cfg["packages"] = {p: {} for p in pkgs}
    save_config(cfg)
    return pkgs


def set_prefix(new_prefix):
    cfg = load_config()
    cfg["package_prefix"] = new_prefix
    save_config(cfg)
