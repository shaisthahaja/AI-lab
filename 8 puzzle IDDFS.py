def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def depth_limited_search(state, goal, limit, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    for next_state in get_neighbors(state):

        if next_state not in path:

            result = depth_limited_search(
                next_state,
                goal,
                limit - 1,
                path + [next_state]
            )

            if result is not None:
                return result

    return None


def IDDFS(start, goal):
    depth = 0

    while True:
        result = depth_limited_search(
            start,
            goal,
            depth,
            [start]
        )

        if result is not None:
            return result

        depth += 1


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = IDDFS(start, goal)

print("Solution:")
for state in solution:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
