# Step-1

adjacency_list = {   # actual cost g
    'S': [('A', 1), ('B', 4),],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
    'G': [('C', 4)],
}

H = {   # huristic cost h
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'G': 0,
}

# Step-2

class Node:
    def __init__(self, nodename, parent, g, h):
        self.name = nodename
        self.parent = parent
        self.g = g   # actual cost g(n)
        self.h = h   # huristic cost h(n)
        self.f = g + h  # f(n)

# Step-3

priority_queue = [] # empty list

def push_sort(node):  # push (insert) node and sort the priority queue (list)
    priority_queue.append(node)
    priority_queue.sort(key = lambda x: x.f)

def is_empty():
    return len(priority_queue) == 0

NOb = Node('S', None, 0, H['S'])   # source Node and parent = none
push_sort(NOb)  # insert source node

while not is_empty():
    NOb = priority_queue.pop(0)
    if NOb.name == 'G':
        break

    for neighbor in adjacency_list[NOb.name]:
        new_node = Node(nodename = neighbor[0], parent = NOb, g = NOb.g+neighbor[1], h = H[neighbor[0]])
        push_sort(new_node)
    NOb = None

# Step-4

path = []
cost = NOb.g

while NOb.parent is not None:
    path.insert(0, NOb.name)
    NOb = NOb.parent

path.insert(0, NOb.name)

print("Path result of A* graph search :", path)
print("Path Cost = ", cost)                    

