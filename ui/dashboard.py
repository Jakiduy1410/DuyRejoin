import time

def draw_dashboard(win, states):
    """
    states = {
      pkg: {
        "status": "RUNNING",
        "since": timestamp or None
      }
    }
    """
    win.erase()
    win.box()
    win.addstr(1, 2, "DASHBOARD")

    # Header row
    win.addstr(3, 2, "Package".ljust(30))
    win.addstr(3, 34, "Status".ljust(10))
    win.addstr(3, 46, "Timer")

    win.hline(4, 1, "-", win.getmaxyx()[1] - 2)

    y = 5
    now = time.time()

    for pkg, info in states.items():
        status = info.get("status", "UNKNOWN")
        since = info.get("since")

        if since:
            elapsed = int(now - since)
            timer = f"{elapsed//60:02}:{elapsed%60:02}"
        else:
            timer = "--"

        win.addstr(y, 2, pkg.ljust(30))
        win.addstr(y, 34, status.ljust(10))
        win.addstr(y, 46, timer)
        y += 1

    win.refresh()
