from collections import deque

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MOVES = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}

def get_neighbors(state):
    neighbors = []

    zero_pos = state.index(0)
    row = zero_pos // 3
    col = zero_pos % 3

    if row > 0:
        new_pos = zero_pos - 3
        new_state = list(state)
        new_state[zero_pos], new_state[new_pos] = \
            new_state[new_pos], new_state[zero_pos]
        neighbors.append(("Up", tuple(new_state)))

    if row < 2:
        new_pos = zero_pos + 3
        new_state = list(state)
        new_state[zero_pos], new_state[new_pos] = \
            new_state[new_pos], new_state[zero_pos]
        neighbors.append(("Down", tuple(new_state)))

    if col > 0:
        new_pos = zero_pos - 1
        new_state = list(state)
        new_state[zero_pos], new_state[new_pos] = \
            new_state[new_pos], new_state[zero_pos]
        neighbors.append(("Left", tuple(new_state)))

    if col < 2:
        new_pos = zero_pos + 1
        new_state = list(state)
        new_state[zero_pos], new_state[new_pos] = \
            new_state[new_pos], new_state[zero_pos]
        neighbors.append(("Right", tuple(new_state)))

    return neighbors


def solve_puzzle(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        # Goal reached
        if state == GOAL:
            return path

        # Generate next states
        for move, new_state in get_neighbors(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(move, new_state)]))

    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = solve_puzzle(start)

if solution:
    print("Initial State:")
    print_state(start)

    print("Solution:")

    for step, (move, state) in enumerate(solution, 1):
        print("Step", step, ":", move)
        print_state(state)

    print("Total moves:", len(solution))
else:
    print("No solution exists.")