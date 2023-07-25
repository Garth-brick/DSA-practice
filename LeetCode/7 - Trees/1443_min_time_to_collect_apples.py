from typing import Dict, List, Set


def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    visited = set()
    children: Dict[int, Set[int]] = {i:set() for i in range(n)}
    for edge in edges:
        children[edge[0]].add(edge[1])
        children[edge[1]].add(edge[0])


    def dfs(root) -> int:
        if root >= n or root in visited:
            return 0

        visited.add(root)
        
        result = 0

        for child in children[root]:
            result += dfs(child)
        if (hasApple[root] or result) and root:
            # if (the chidren had apples and this isn't the root node) or (this node has apples itself)
            result += 2
        return result
        
    return dfs(0)

true = True
false = False
edges: List[List[int]] = [[0,2],[0,3],[1,2]]
hasApple: List[bool] = [false,true,false,false]
print(minTime(4, edges, hasApple))