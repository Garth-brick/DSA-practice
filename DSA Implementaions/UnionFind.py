from typing import List


class UnionFindInt:
    
    def __init__(self, size: int) -> None:
        self.rank: List[int] = [1] * size
        self.parent: List[int] = [i for i in range(size)]
        self._components = size
        
    @property
    def components(self):
        return self._components
        
    def find(self, n: int) -> int:
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, n1: int, n2: int) -> bool:
        p1: int = self.find(n1)
        p2: int = self.find(n2)
        
        if p1 == p2:
            return False
        
        self._components -= 1
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p1] = self.rank[p2]
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
            self.rank[p2] = self.rank[p1]
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
            self.rank[p1] = self.rank[p2]
            
        return True
    
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)