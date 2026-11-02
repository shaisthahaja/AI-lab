import heapq

N = 8

def heuristic(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def astar():
    pq = [(0, 0, [])]
    visited = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        if len(state) == N and heuristic(state) == 0:
            return state

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        row = len(state)

        for col in range(N):
            if all(state[i] != col and
                   abs(state[i] - col) != abs(i - row)
                   for i in range(row)):

                new_state = state + [col]
                new_g = g + 1
                new_f = new_g + heuristic(new_state)

                heapq.heappush(pq, (new_f, new_g, new_state))

    return None

solution = astar()

print("Solution:")
for col in solution:
    print(" ".join("Q" if j == col else "." for j in range(N)))