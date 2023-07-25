class PriorityQueue:
    
    def __init__(self) -> None:
        self.heap: list = []

    def __str__(self) -> str:
        return "[" + ", ".join([str(i) for i in self.heap]) + "]"
    
    def __len__(self) -> int:
        return len(self.heap)
        
    def __getitem__(self, i: int):
        assert isinstance(i, int), "Indexes must be of type int"
        assert i >= 0 and i < len(self), "Indexes must be greater than zero and less than the length"
        return self.heap[i]
    
    def __parentIndex(self, i: int) -> int:
        return (i-1) // 2
    
    def __leftChildIndex(self, i: int) -> int:
        return (i *2) + 1
    
    def __rightChildIndex(self, i: int) -> int:
         return (i * 2) + 2
     
    def __swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __siftUp(self, i: int):
        while i > 0 and self.heap[i] < self.heap[self.__parentIndex(i)]:
            parentIndex = self.__parentIndex(i)
            self.__swap(i, parentIndex)
            i = parentIndex
    
    def __siftDown(self, i: int) -> None:
        if i < 0 or i >= len(self): return
        
        l: int = self.__leftChildIndex(i)
        r: int = self.__rightChildIndex(i)
        smallest: int = i
        
        if (l < len(self) and self.heap[l] < self.heap[smallest]):
            smallest = l
        if (r < len(self) and self.heap[r] < self.heap[smallest]):
            smallest = r
        if not smallest == i:
            self.__swap(i, smallest)
            return self.__siftDown(smallest)
        
    
    def isEmpty(self) -> bool:
        return len(self.heap)==0
    
    def insert(self, val) -> None:
        self.heap.append(val)
        self.__siftUp(len(self) - 1)

    def heaptop(self):
        assert not self.isEmpty()
        return self[0]
    
    def heappop(self):
        assert not self.isEmpty(), "can't pop from an empty heap"
        
        minItem = self.heaptop()
        self.__swap(0, len(self)-1)
        self.heap.pop()
        self.__siftDown(0)
        return minItem
    
    
heap = PriorityQueue()
heap.insert(3)
heap.insert(1)
heap.insert(5)
heap.insert(-1)
heap.insert(4)
print(heap)
print(heap.heappop())
print(heap.heappop())
print(heap.heappop())
print(heap.heappop())
print(heap.heappop())