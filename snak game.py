import random  # Import the random module
import curses  # Import the curses module

def main(screen):
    curses.curs_set(0)  # Hide the cursor
    screen_height, screen_width = screen.getmaxyx()  # Get the screen height and width
    window = curses.newwin(screen_height, screen_width, 0, 0)  # Create a new window
    window.keypad(1)  # Enable keypad mode
    window.timeout(100)  # Refresh every 100 milliseconds

    snk_x = screen_width // 4
    snk_y = screen_height // 2

    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    food = [screen_height // 2, screen_width // 2]
    window.addch(food[0], food[1], curses.ACS_PI)  # Add food

    key = curses.KEY_RIGHT  # Initial direction

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        # Check if snake hits wall or itself
        if (snake[0][0] in [0, screen_height - 1] or
            snake[0][1] in [0, screen_width - 1] or
            snake[0] in snake[1:]):
            curses.endwin()
            quit()

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, screen_height - 2),
                    random.randint(1, screen_width - 2)
                ]
                food = nf if nf not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


curses.wrapper(main)
