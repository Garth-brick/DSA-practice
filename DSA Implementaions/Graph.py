import collections
from typing import Any, Dict, List, Set, Tuple


""" NOTE
- Implementing a graph data structure using a GraphNode objects as vertices and a globally accessible list of all the edges in the graph
"""



class Graph:
    
    class GraphNode:
        
        def __init__(self, val: Any):
            self.val = val
            
        def __hash__(self) -> int:
            return hash((self.val, id(self)))
        
        def __eq__(self, other) -> bool:
            if isinstance(other, Graph.GraphNode):
                return self.val == other.val
            return False
        
        def __lt__(self, other: 'Graph.GraphNode') -> bool:
            return self.val < other.val
        
        def __repr__(self) -> str:
            return f"GN:{self.val}"
        
        def __str__(self) -> str:
            return f"{self.val}"
    
    def __init__(self) -> None:
        
        # [all vertices in the graph]
        self._vertices: Set[Graph.GraphNode] = set()
        
        # {vertex: {set of neighbours}}
        self._neighborList: Dict[Graph.GraphNode, Set[Graph.GraphNode]] = {}
    
    def __len__(self) -> int:
        return len(self._vertices)
    
    def __bool__(self) -> bool:
        return bool(len(self))
    
    def createVertex(self, val: Any) -> 'Graph.GraphNode':
        # creatiing a new GraphNode from the given value
        newGraphNode = Graph.GraphNode(val)
        
        # adding the new vertex to set of vertices
        self._vertices.add(newGraphNode)
        
        # addinng the new vertex as a key to the edglist without any neighbors
        self._neighborList[newGraphNode] = set()
        
        return newGraphNode
    
    def removeVertex(self, vertex: 'Graph.GraphNode') -> Any:
        # remove it from the list of vertices
        self._vertices.remove(vertex)
        
        # remove all of its outgoing edges
        self._neighborList.pop(vertex)
        
        # remove all incoming edges
        for neighbors in self._neighborList.values():
            neighbors.discard(vertex)
    
    def addEdge(self, vertex: 'Graph.GraphNode', neighbor: 'Graph.GraphNode', birectional: bool=False) -> None:
        assert vertex in self._vertices, f"vertex {vertex} is not present in this graph"
        assert neighbor in self._vertices, f"vertex {neighbor} is not present in this graph"
        
        # add a new neighbor to the vertex
        self._neighborList[vertex].add(neighbor)
        
        # if we want a bidirectional graph then connect the edge back from the neighbor as well
        if birectional:
            self._neighborList[neighbor].add(vertex)
    
    # returns a list with lists of vertices which were discovered in separate iterations of BFS
    def bfsFromValues(self, *rootVertexVals) -> List[List['Graph.GraphNode']]:
        if not self or not rootVertexVals:
            # if there are no nodes in the graph or no source values given
            return []
        
        q: collections.deque['Graph.GraphNode'] = collections.deque()
        visited: Set['Graph.GraphNode'] = set()
        
        for vertex in self._vertices:
            if vertex.val in rootVertexVals:
                q.append(vertex)
                visited.add(vertex)
        
        output: List[List[Graph.GraphNode]] = []
        
        while q:
            level = []
            for _ in range(len(q)):
                vertex = q.popleft()
                level.append(vertex)
                
                neighbors = self._neighborList[vertex]
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    q.append(neighbor)
            output.append(level)

        return output
    
    def bfs(self, root: 'Graph.GraphNode') -> List['Graph.GraphNode']:
        if root not in self._vertices:
            return []
        
        q: collections.deque[Graph.GraphNode] = collections.deque()
        q.append(root)
        visited: Set[Graph.GraphNode] = set()
        visited.add(root)
        
        output = []
        
        while q:
            vertex = q.popleft()
            output.append(vertex)
            for neighbor in self._neighborList[vertex]:
                if neighbor in visited:
                    continue
                q.append(neighbor)
                visited.add(neighbor)
        
        return output
    
    # returns a list with the in the order in which the vertices were discovered during DFS
    def dfs(self, root: 'Graph.GraphNode') -> List['Graph.GraphNode']:
        stack: List[Graph.GraphNode] = []
        stack.append(root)
        visited: Set[Graph.GraphNode] = set()
        visited.add(root)
        
        output: List[Graph.GraphNode] = []
        
        while stack:
            vertex = stack.pop()
            output.append(vertex)
            for neighbor in self._neighborList[vertex]:
                if neighbor in visited:
                    continue
                stack.append(neighbor)
                visited.add(neighbor)
        
        return output
            
    def dfsRecursive(self, vertex: 'Graph.GraphNode', visited: Set['Graph.GraphNode']=set(), output: List['Graph.GraphNode']=[]):
        visited.add(vertex)
        output.append(vertex)
        
        for neighbor in self._neighborList[vertex]:
            if neighbor in visited:
                continue
            self.dfsRecursive(neighbor, visited, output)
        
        return output   
    
    # this will fail to be correct if there is a cycle
    def topologicalSort(self) -> List['Graph.GraphNode']:
        
        output: List[Graph.GraphNode] = []
        visited: Set[Graph.GraphNode] = set()
        
        def _topoloicalSortHelper(root):
            stack: List[Graph.GraphNode] = []
            stack.append(root)
            visited.add(root)
            
            while stack:
                # popping the most recently added vertex to check its neighbors
                vertex = stack.pop()
                for neighbor in self._neighborList[vertex]:
                    if neighbor in visited:
                        continue
                    
                    # if there are any unvisited neighbors then we need to put the vertex back in the stack
                    # this is because we want to only remove a vertex from the stack after all its neighbors are visited
                    stack.append(vertex)
                    
                    # append unvisited neighbors and mark them visited
                    stack.append(neighbor)
                    visited.add(neighbor)
                    break
                else:
                    # this block only gets executed if the above loop did not get a 'break'
                    # the vertex will only get added to the output if it had no unvisited neighbors
                    output.append(vertex)
            
        # go over all vertices to make sure to not miss any one
        for vertex in self._vertices:
            if vertex not in visited:
                _topoloicalSortHelper(vertex)

        # appending to the right leads to elements that should be at the end coming first
        output.reverse()
        return list(output)
    
g = Graph()
va = g.createVertex("a")
vb = g.createVertex("b")
vc = g.createVertex("c")
vx = g.createVertex("X")
g.addEdge(va, vb)
g.addEdge(va, vc)
g.addEdge(vb, vx)
g.addEdge(vc, vx)

# for vertex in g.vertices:
print(g.topologicalSort())