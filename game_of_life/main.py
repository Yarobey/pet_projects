import random

DEAD, ALIVE = 0, 1

def dead_state(width, height):
    """Returns a matrix of size WIDTHxHEIGHT with all DEAD cells
    that represents dead board

    >>> dead_state(0,0)
    []
    >>> dead_state(5,4)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    """
    return [[DEAD for _ in range(width)] for _ in range(height)]

def random_state(width, height):
    """Returns board state in which every cell has been randomly initialized
    to either ALIVE or DEAD
    """
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            random_number = random.random()
            state[i][j] = DEAD if random_number >= 0.5 else ALIVE
    return state

def render(state):
    """Formats the random_state board and prints
    the STATE to the terminal
    """

    height, width = len(state), len(state[0])
    print('@'*(width+2))
    for i in range(height):
        out_str = ''
        for j in range(width):
            char = ' ' if state[i][j] == DEAD else '*'
            out_str += char
        print('@'+out_str+'@')
    print('@'*(width+2))

def next_board_state(initial_state):
    """Calculates the next board state based on the rules:
    1. Any live cell with 0 or 1 live neighbors becomes DEAD, because of underpopulation
    2. Any live cell with 2 or 3 live neighbors stays ALIVE, because its neighborhood is just right
    3. Any live cell with more than 3 live neighbors becomes DEAD, because of overpopulation
    4. Any dead cell with exactly 3 live neighbors becomes ALIVE, by reproduction
    """
    dx = (-1, -1, 0, 1, 1, 1, 0, -1)
    dy = (0, 1, 1, 1, 0, -1, -1, -1)
    next_state = []
    height, width = len(initial_state)+2, len(initial_state[0])+2

    # Creating a boarder for the initial state board
    initial_state = [list('@'*width)] + initial_state + [list('@'*width)]
    for i in range(1, height-1):
        initial_state[i] = ['@'] + initial_state[i] + ['@']

    # Calculating the next state
    for i in range(1, height-1):
        new_row = []
        for j in range(1, width-1):
            alive_count = 0
            for k in range(8):
                if initial_state[i+dx[k]][j+dy[k]] == ALIVE:
                    alive_count += 1
            # Following the rules
            if alive_count not in (2,3):
                new_row.append(DEAD)
                continue
            if (initial_state[i][j] == DEAD) and (alive_count == 2):
                new_row.append(DEAD)
                continue
            new_row.append(ALIVE)
        next_state.append(new_row)

    return next_state

def load_board_state(input_path):
    init_state = []
    file = open(input_path, "r")
    for line in file:
        new_row = []
        for char in line:
            if char != "\n":
                new_row.append(int(char))
        init_state.append(new_row)
    file.close()
    return init_state

# state = random_state(100, 73)
# state = load_board_state("toad.txt")
# state = load_board_state("beacon.txt")
# state = load_board_state("blinker.txt")
# state = load_board_state("glider.txt")
state = load_board_state("gosper_glider_gun.txt")

while True:
    render(state)
    state = next_board_state(state)
