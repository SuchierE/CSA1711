from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if jug1 == target or jug2 == target:
            print("Solution found:\n")
            for step in path:
                print(step)
            print(f"Final State: ({jug1}, {jug2})")
            return

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        queue.append((
            capacity1,
            jug2,
            path + [f"Fill Jug 1 -> ({capacity1}, {jug2})"]
        ))

        queue.append((
            jug1,
            capacity2,
            path + [f"Fill Jug 2 -> ({jug1}, {capacity2})"]
        ))

        queue.append((
            0,
            jug2,
            path + [f"Empty Jug 1 -> (0, {jug2})"]
        ))

        queue.append((
            jug1,
            0,
            path + [f"Empty Jug 2 -> ({jug1}, 0)"]
        ))

        amount = min(jug1, capacity2 - jug2)
        queue.append((
            jug1 - amount,
            jug2 + amount,
            path + [
                f"Pour Jug 1 -> Jug 2 -> ({jug1 - amount}, {jug2 + amount})"
            ]
        ))

        amount = min(jug2, capacity1 - jug1)
        queue.append((
            jug1 + amount,
            jug2 - amount,
            path + [
                f"Pour Jug 2 -> Jug 1 -> ({jug1 + amount}, {jug2 - amount})"
            ]
        ))

    print("No solution exists.")


water_jug(4, 3, 2)