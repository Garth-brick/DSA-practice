import queue
import collections

# THIS LEADS TO APPENDING THE NODE MULTIPLE TIMES IF THERE ARE MULTIPLE PATHS TO IT

def shortestPath(graph: collections.defaultdict[str, list[tuple[str, int]]], SOURCE: str, TARGET: str):
    pq: queue.PriorityQueue[tuple[int, str]] = queue.PriorityQueue()
    pq.put((0, SOURCE))
    
    while not pq.empty():
        cost, vertex = pq.get()
        if vertex is TARGET:
            return cost
        for nei, wt in graph[vertex]:
            pq.put((cost + wt, nei))
    return -1
    

bidirectional = False
graph: collections.defaultdict[str, list[tuple[str, int]]] = collections.defaultdict(list)
VERTEX_COUNT, EDGE_COUNT = map(int, input().strip().split())
for _ in range(EDGE_COUNT):
    v1, v2, w = input().strip().split()
    graph[v1].append((v2, int(w)))
    if bidirectional:
        graph[v2].append((v1, int(w)))
SOURCE, TARGET = input().strip().split()


result = shortestPath(graph, SOURCE, TARGET)
if result != -1:
    print(f"Shortest distance from {SOURCE} to {TARGET} is {result}")
else:
    print("No such path")

"""input
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
A D
"""