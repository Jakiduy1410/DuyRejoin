import curses
import threading
import time

from core.packages import get_packages_by_prefix
from core.auto_rejoin import auto_rejoin_loop

auto_running = False
auto_thread = None


def main(stdscr):
    global auto_running, auto_thread

    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    h, w = stdscr.getmaxyx()

    # ===== STATIC UI (DRAW ONCE) =====
    stdscr.box()
    stdscr.addstr(1, 2, "AUTO TOOL V5 - ZAM STYLE")
    stdscr.hline(2, 1, "-", w - 2)

    stdscr.addstr(3, 2, "[1] Start Auto Rejoin")
    stdscr.addstr(4, 2, "[2] Scan Packages")
    stdscr.addstr(5, 2, "[3] Set GameID (CLI)")
    stdscr.addstr(6, 2, "[4] Detect UserID (CLI)")
    stdscr.addstr(7, 2, "[0] Exit")

    stdscr.hline(8, 1, "-", w - 2)

    # ===== LOG WINDOW =====
    log_h = h - 10
    logw = curses.newwin(log_h, w - 4, 9, 2)
    logw.scrollok(True)
    logw.idlok(True)

    logw.addstr("LOG:\n")
    logw.refresh()
    stdscr.refresh()

    stdscr.timeout(500)

    # ===== LOGGER FUNCTION =====
    def logger(msg):
        try:
            logw.addstr(msg + "\n")
            logw.refresh()
        except curses.error:
            pass

    # ===== AUTO REJOIN THREAD =====
    def auto_worker():
        logger("[AUTO] Auto Rejoin started")
        auto_rejoin_loop(logger)

    # ===== EVENT LOOP =====
    while True:
        key = stdscr.getch()

        if key == ord('1') and not auto_running:
            auto_running = True
            auto_thread = threading.Thread(
                target=auto_worker,
                daemon=True
            )
            auto_thread.start()
            logger("[UI] Start Auto Rejoin")

        elif key == ord('2'):
            pkgs = get_packages_by_prefix()
            logger("[SCAN] Found packages:")
            for p in pkgs:
                logger(f"  - {p}")

        elif key == ord('0'):
            break

        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(main)
