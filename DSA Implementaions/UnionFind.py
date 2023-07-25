from typing import List


class UnionFind:
    
    def __init__(self, size: int):
        self.size: int = size
        self.parent: List[int] = [i for i in range(size)]
        self.rank: List[int] = [1 for _ in range(size)]
        self._components: int = size
        
    @property
    def components(self):
        return self._components
        
    def find(self, i):
        assert i in range(self.size), "index out of bounds"
        
        while i != self.parent[i]:
            p = self.parent[i]
            self.parent[i] = self.parent[p]
            i = p
        return self.parent[i]
    
    def union(self, n1, n2):
        assert n1 in range(self.size), "index out of bounds"
        assert n2 in range(self.size), "index out of bounds"
        
        p1: int = self.find(n1)
        p2: int = self.find(n2)
        
        if self.isConnected(p1, p2):
            return
        
        self._components -= 1
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
    
    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)