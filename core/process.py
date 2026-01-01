import subprocess

def is_running(pkg):
    return bool(subprocess.getoutput(f"pidof {pkg}"))

def force_stop(pkg):
    subprocess.run(
        ["am", "force-stop", pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def start_app(pkg, uri):
    subprocess.run(
        [
            "am", "start",
            "-a", "android.intent.action.VIEW",
            "-d", uri,
            "-p", pkg,
            "--user", "0"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
