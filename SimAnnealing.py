
import random
import math

N = 8

# Calculate attacking pairs of queens
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


# Generate a random neighboring state
def random_neighbor(state):
    new_state = state.copy()

    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)

    while new_state[col] == row:
        row = random.randint(0, N - 1)

    new_state[col] = row
    return new_state


# Simulated Annealing algorithm
def simulated_annealing(initial_state):
    current = initial_state.copy()

    T = 1000
    cooling_rate = 0.995
    min_temperature = 0.001

    while T > min_temperature:

        if heuristic(current) == 0:
            return current

        next_state = random_neighbor(current)

        delta_E = heuristic(current) - heuristic(next_state)

        if delta_E > 0:
            current = next_state
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        T *= cooling_rate

    if heuristic(current) == 0:
        return current

    return None


# Run the algorithm with random restarts
while True:
    initial_state = [random.randint(0, N - 1)
                     for _ in range(N)]

    solution = simulated_annealing(initial_state)

    if solution is not None:
        break

print("Initial State:", initial_state)

print("\nFinal State:")
display(solution)

print("\nSolution:", solution)
print("Final Heuristic:", heuristic(solution))
