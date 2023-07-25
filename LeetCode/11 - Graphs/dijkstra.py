""" NOTE
- Single source shortest path
- Uses a greedy approach
- For all source look at Floyd-Warshall (uses a dynamic programming approach)
"""

import heapq
import collections
from typing import List, Tuple

# THIS LEADS TO APPENDING THE NODE MULTIPLE TIMES IF THERE ARE MULTIPLE PATHS TO IT

def shortestPath(
    graph: collections.defaultdict[str, List[Tuple[str, int]]], 
    SOURCE: str, 
    TARGET: str
    ):
    
    # put the cost first because we want the heap to be ordered by the cost
    heap: List[Tuple[int, str]] = []
    heapq.heappush(heap, (0, SOURCE))
    
    # heappop will return the vertex with the least cost which we can take next
    
    while heap:
        cost, vertex = heapq.heappop(heap)
        if vertex == TARGET:
            return cost
        for neighbor, edgeWeight in graph[vertex]:
            heapq.heappush(heap, (cost + edgeWeight, neighbor))
            
    return -1


graph: collections.defaultdict[str, List[Tuple[str, int]]] = collections.defaultdict(list)
V, E = map(int, input().strip().split())
for _ in range(E):
    v1, v2, w = input().strip().split()
    graph[v1].append((v2, int(w)))
SOURCE, TARGET = input().strip().split()
print(shortestPath(graph, SOURCE, TARGET))

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