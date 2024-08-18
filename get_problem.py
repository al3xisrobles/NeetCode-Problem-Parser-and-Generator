import curses
import pandas as pd

# Load the CSV data
df = pd.read_csv('parsed_neetcode.csv')

def select_items(stdscr, items, title):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0, 0, title[:curses.COLS-1])
    current_row = 0

    selected_items = [False] * len(items)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title[:curses.COLS-1])
        for idx, item in enumerate(items):
            x = 0
            y = idx + 1
            if y >= curses.LINES:
                break
            display_str = item[:curses.COLS-5]
            if idx == current_row:
                stdscr.addstr(y, x, display_str, curses.color_pair(1))
            else:
                stdscr.addstr(y, x, display_str)
            if selected_items[idx]:
                stdscr.addstr(y, x + len(display_str) + 1, "[X]", curses.color_pair(2))
            else:
                stdscr.addstr(y, x + len(display_str) + 1, "[ ]", curses.color_pair(2))

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(items) - 1:
            current_row += 1
        elif key == ord(' '):
            selected_items[current_row] = not selected_items[current_row]
        elif key == ord('\n'):
            break

    selected_items_list = [item for idx, item in enumerate(items) if selected_items[idx]]
    return selected_items_list

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()

    categories = df['Category'].unique().tolist()
    difficulties = df['Difficulty'].unique().tolist()

    selected_categories = select_items(stdscr, categories, "Select Categories (use UP/DOWN to navigate, SPACE to select, ENTER to confirm):")
    selected_difficulties = select_items(stdscr, difficulties, "Select Difficulties (use UP/DOWN to navigate, SPACE to select, ENTER to confirm):")

    while True:
        filtered_df = df[(df['Category'].isin(selected_categories)) &
                         (df['Difficulty'].isin(selected_difficulties)) &
                         (df['CompletedWithThisScript'] == False)]

        if filtered_df.empty:
            stdscr.clear()
            stdscr.addstr(0, 0, "No more questions available in the selected categories and difficulties.", curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            break

        selected_question = filtered_df.sample().iloc[0]

        stdscr.clear()
        problem_str = f"Problem: {selected_question['Problem']}"
        link_str = f"Link: {selected_question['Link']}"
        stdscr.addstr(0, 0, problem_str[:curses.COLS-1])
        stdscr.addstr(1, 0, link_str[:curses.COLS-1])
        stdscr.addstr(2, 0, "Press ENTER when you have solved the problem.")

        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key != curses.KEY_RESIZE:
                break

        df.loc[df['Problem'] == selected_question['Problem'], 'CompletedWithThisScript'] = True
        df.to_csv('parsed_neetcode.csv', index=False)

curses.wrapper(main)
