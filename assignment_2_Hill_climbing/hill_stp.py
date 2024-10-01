import math

def list_Initialize():
    list = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    return list

def calculate_cost(state):     # inversion counting
    countingInversation = 0

    for i in range(len(state) - 1):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                countingInversation += 1

    return countingInversation

def generate_neighbors(current_state):    # generate neighbopur
    neighbors = []

    for i in range(len(current_state) - 1):
        new_list = current_state.copy()
        for j in range(i, len(current_state) - 1):
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
            neighbors.append(new_list.copy())
    return neighbors

def state_generation(current_state):   # state generation
    while True:
        current_state_cost = calculate_cost(current_state)
        print("Current State:", current_state, "Cost :", current_state_cost)
        min_next_cost = math.inf
        min_next_state = None

        neighbors = generate_neighbors(current_state) # change start for steepest ascent

        for i in range(len(neighbors)):
            next_state = neighbors[i]
            next_state_cost = calculate_cost(next_state)
            if next_state_cost < min_next_cost:
                min_next_cost = next_state_cost
                min_next_state = next_state

        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print("Final State:", current_state, "Cost :", current_state_cost)
            break

def main():
    initial_state = list_Initialize()
    state_generation(initial_state)
    print("Finished successfully.....")

if __name__ == "__main__":
    main()