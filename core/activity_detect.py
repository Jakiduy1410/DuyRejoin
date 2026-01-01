import subprocess

def get_launch_activity(pkg):
    cmd = f"cmd package resolve-activity --brief {pkg}"
    out = subprocess.getoutput(cmd).strip()

    # output thường dạng:
    # com.zamdepzai.clienx/com.roblox.client.startup.ActivitySplash
    if "/" in out:
        return out.split("/")[1]

    return None
