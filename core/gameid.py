import json

CONFIG = "config/config.json"


def load_config():
    with open(CONFIG) as f:
        return json.load(f)


def save_config(cfg):
    with open(CONFIG, "w") as f:
        json.dump(cfg, f, indent=2)


def set_game_id(pkg, place_id):
    cfg = load_config()
    cfg["game_ids"][pkg] = f"roblox://placeID={place_id}"
    save_config(cfg)


def get_game_uri(pkg):
    cfg = load_config()
    return cfg["game_ids"].get(pkg)
