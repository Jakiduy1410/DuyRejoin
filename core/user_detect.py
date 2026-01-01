import subprocess


def detect_user_id(pkg):
    out = subprocess.getoutput(f"dumpsys package {pkg} | grep userId")
    return out.strip() if out else None
