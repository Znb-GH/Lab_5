# ==============================================================
# LAB 5 - BREADTH FIRST SEARCH (BFS)
# Task 1, Task 2 and Task 3 
# ==============================================================

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = []
        for i in range(V):
            self.adj.append([])

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def bfs(self, s):
        visited = []
        for i in range(self.V):
            visited.append(False)

        queue = []
        visited[s] = True
        queue.append(s)

        while len(queue) > 0:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in self.adj[s]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    queue.append(neighbour)

        print()

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(1, 0)

g.add_edge(0, 4)
g.add_edge(4, 0)

g.add_edge(1, 2)
g.add_edge(2, 1)

g.add_edge(1, 3)
g.add_edge(3, 1)

g.add_edge(1, 4)
g.add_edge(4, 1)

g.add_edge(2, 3)
g.add_edge(3, 2)

g.add_edge(3, 4)
g.add_edge(4, 3)

print("Graph (each vertex and its neighbours):")
for vertex in range(g.V):
    print(" ", vertex, "->", g.adj[vertex])

print("\nFollowing is Breadth First Traversal (starting from vertex 0):")
g.bfs(0)




#task 2
print()
print("=" * 50)
print("TASK 2: BFS on the tree (start = A, goal = G)")
print("=" * 50)

tree = {
    "A": ["B", "F", "D", "E"],
    "B": ["K", "J"],
    "F": [],
    "D": ["G"],
    "E": ["C", "H", "I"],
    "K": ["N", "M"],
    "J": [],
    "G": [],
    "C": [],
    "H": [],
    "I": ["L"],
    "N": [],
    "M": [],
    "L": [],
}

def bfs_find_goal(tree, start_node, goal_node):
    queue = []
    visit_order = []
    came_from = {start_node: None}

    queue.append(start_node)

    while len(queue) > 0:
        current_node = queue.pop(0)
        visit_order.append(current_node)

        if current_node == goal_node:
            path = []
            node = goal_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            return visit_order, path

        for child in tree[current_node]:
            if child not in came_from:
                came_from[child] = current_node
                queue.append(child)

    return visit_order, None

start_node = "A"
goal_node = "G"
visit_order, path = bfs_find_goal(tree, start_node, goal_node)

print("Visit order :", visit_order)
if path is not None:
    print("Goal", goal_node, "found!")
    print("Path :", path)
else:
    print("Goal", goal_node, "was not found")
#task 3
print()
print("=" * 50)
print("TASK 3: Priority Queue")
print("=" * 50)

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, name, priority):
        self.items.append((priority, name))
        self.items.sort()

    def remove(self):
        if self.is_empty():
            return None
        priority, name = self.items.pop(0)
        return name, priority

    def peek(self):
        if self.is_empty():
            return None
        priority, name = self.items[0]
        return name, priority

    def size(self):
        return len(self.items)

my_queue = PriorityQueue()

my_queue.add("Write report", 3)
my_queue.add("Fix server crash", 1)
my_queue.add("Reply to email", 4)
my_queue.add("Prepare exam", 2)

print("Number of items in the queue:", my_queue.size())
print("Next item to come out :", my_queue.peek())

print("\nRemoving items:")
while not my_queue.is_empty():
    name, priority = my_queue.remove()
    print(" Removed:", name, "-> priority", priority)