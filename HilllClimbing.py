
import random

N = 4

# Calculate the number of attacking pairs
def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Display chessboard
def display(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print()


# Generate all possible successors
def successors(state):
    result = []

    for col in range(N):
        for row in range(N):
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                result.append(new_state)

    return result


# Steepest-ascent hill climbing
def hill_climbing(initial_state):
    current = initial_state.copy()

    print("Initial State:")
    display(current)
    print("Initial Heuristic:", heuristic(current))

    while True:
        neighbors = successors(current)

        # Find the best successor
        best = min(neighbors, key=heuristic)

        # Stop if no improvement is possible
        if heuristic(best) >= heuristic(current):
            if heuristic(current) == 0:
                print("Solution Found!")
                return current
            else:
                print("Local Maximum Reached. Restarting...")
                return None

        current = best

    return current


# Random restart until solution is found
initial_state = [0, 1, 2, 3]

while True:
    solution = hill_climbing(initial_state)

    if solution is not None:
        break

    initial_state = [random.randint(0, 3) for _ in range(N)]

print("\nFinal State:")
display(solution)
print("Final Heuristic:", heuristic(solution))
