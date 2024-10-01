import math

def list_Initialize():
    list = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    return list

def cost_calculation(state):    # inversion counting 
    countingInversation = 0

    for i in range(len(state) - 1):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                countingInversation += 1

    return countingInversation

def generate_neighbors(current_state):   # generate neighbopur
    neighbors = []

    for i in range(len(current_state) - 1):
        new_list = current_state.copy()
        for j in range(i, len(current_state) - 1):
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
            neighbors.append(new_list.copy())
    return neighbors

def State_generation(current_state):    # state generation
    while True:
        current_state_cost = cost_calculation(current_state)
        print("Current State :" , current_state, "Cost :", current_state_cost)
        min_next_cost = math.inf
        min_next_state = None

        for neighbor in generate_neighbors(current_state):  # change start for first choice
            next_state_cost = cost_calculation(neighbor)

            if next_state_cost < current_state_cost:
                min_next_cost = next_state_cost
                min_next_state = neighbor
                break

        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print("Final State:", current_state, "Cost :", current_state_cost)
            break

def main():
    initial_state = list_Initialize()
    State_generation(initial_state)
    print("Finished successfully.....")

if __name__ == "__main__":
    main()