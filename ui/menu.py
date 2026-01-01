import curses

MENU_ITEMS = [
    "[1] Set Prefix",
    "[2] Scan Packages",
    "[3] Set GameID",
    "[4] Detect UserID",
    "[5] Start Auto Rejoin",
    "[0] Exit"
]

def draw_menu(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    box_w = 60
    box_h = len(MENU_ITEMS) + 4
    start_x = (w - box_w) // 2
    start_y = (h - box_h) // 2

    # Box
    stdscr.attron(curses.color_pair(3))
    stdscr.box()
    stdscr.attroff(curses.color_pair(3))

    # Title
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(start_y - 2, start_x, "AutoTool Phase 2 - Menu")
    stdscr.attroff(curses.A_BOLD)

    # Menu
    y = start_y
    for item in MENU_ITEMS:
        stdscr.addstr(y, start_x + 2, item)
        y += 1

    stdscr.addstr(y + 1, start_x + 2, "Select option:")
    stdscr.refresh()
