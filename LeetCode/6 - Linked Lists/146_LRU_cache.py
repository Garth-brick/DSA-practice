from typing import Optional, Dict


class ListNode:
    
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


""" NOTES
- LRU = least recently used
- This is actually how browsers work, they remove the cache that was least recently used when they need to add cache that exceeds their capacity.
    - it is important to use this map t be able to access the values from existing keys in O(1) time
- We will need to keep a hashmap to associate each key with a node (the node will have the value)
- We will make a doubly linked list with nodes that represent the key-value pair
- We will keep a left and right pointer to keep track of the most recently used and least recently used nodes
- Every new node will get inserted to the right
- Everytime we need to move a node to make it the most recent node we'll remove it from wherever it is at (we will know the pointers to each node throug the hashmap) and then re-instert it at the right-most position
- Whenever we need to remove a node we'll just remove it from the left
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity

        # hashmap to store the keys with their associated nodes
        self.cache: Dict[int, ListNode] = {}

        # initialising the left and right pointers at dummy nodes for the head and tail
        self.left: ListNode = ListNode() # least recently used
        self.right: ListNode = ListNode() # most recently used, newly constructed also goes here
        self.left.next = self.right 
        self.right.prev = self.left 

    def removeNode(self, node: ListNode):

        # do not remove the dummy nodes at the head or tail of the list
        if (not node.prev) or (not node.next): return

        prevNode: ListNode = node.prev
        nextNode: ListNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del node


    def insertAtRight(self, node: ListNode):

        # this will always insert a node at the rightmost position (since that is the only place where we will need to be inserting nodes in this class anyways)

        if not self.right.prev: return

        prevNode: ListNode = self.right.prev
        prevNode.next = node
        node.next = self.right
        node.prev = prevNode
        self.right.prev = node



    def get(self, key: int) -> int:
        if key in self.cache:
            # updating the position of the key so that it is the mode recently accessed one now
            self.removeNode(self.cache[key])
            self.insertAtRight(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if the key already exists then we just need to update the value of the node associated with it and bring it forward. We can do that by removing the existing key-value pair and then adding a new one
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insertAtRight(self.cache[key])
        
        # if we have too more elements than our capacity then we need to remove elements
        if len(self.cache) > self.capacity:
            if not self.left.next: return

            lru: ListNode = self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]