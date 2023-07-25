from typing import Dict, List, Set, Tuple, Optional

def numberOfPaths(neighborList: Dict[str, List[str]], source: str, target: str):
    
    if source not in neighborList or target not in neighborList:
        return 0
    
    memo: Dict[str, int] = {}
    cycle = set()

    def dfs(node) -> int:
        if node == target:
            return 1
        if node in memo:
            return memo[node]
        
        cycle.add(node)
        result = 0
        for neighbor in neighborList[node]:
            if neighbor in cycle:
                continue
            result += dfs(neighbor)
        cycle.remove(node)
        memo[node] = result
        return result
    
    result = dfs(source)
    print(memo)
    return result
        

V, E = map(int, input().strip().split())
neighborList: Dict[str, List[str]] = {}
for _ in range(E):
    v1, v2 = input().strip().split()
    if v1 not in neighborList:
        neighborList[v1] = []
    if v2 not in neighborList:
        neighborList[v2] = []
    neighborList[v1].append(v2)

source, target = input().split()
print(numberOfPaths(neighborList, source, target))

"""input
4 3
A B
B C
C E
A D
"""