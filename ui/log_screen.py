def draw_log(stdscr, lines):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    stdscr.addstr(1, 2, "AutoTool - Log (Press any key to return)")
    y = 3

    for line in lines[-(h - 5):]:
        stdscr.addstr(y, 2, line[:w-4])
        y += 1

    stdscr.refresh()
