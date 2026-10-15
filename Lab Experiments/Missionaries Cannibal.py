from collections import deque


def solve_missionaries_cannibals():

    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = {start}

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution found:\n")
            for step in path:
                print(step)
            print("Goal reached!")
            return

        for dm, dc in moves:
            if boat == 0:
                new_m = m - dm
                new_c = c - dc
                new_boat = 1
                direction = "Left to Right"
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 0
                direction = "Right to Left"

            if not (0 <= new_m <= 3 and
                    0 <= new_c <= 3):
                continue

            right_m = 3 - new_m
            right_c = 3 - new_c

            if ((new_m > 0 and new_c > new_m) or
                    (right_m > 0 and right_c > right_m)):
                continue

            new_state = (new_m, new_c, new_boat)

            if new_state not in visited:
                visited.add(new_state)
                action = (
                    f"Move {dm} missionary(s) and "
                    f"{dc} cannibal(s) {direction}: "
                    f"{new_state}"
                )
                queue.append(
                    (new_state, path + [action])
                )

    print("No solution exists.")


solve_missionaries_cannibals()
