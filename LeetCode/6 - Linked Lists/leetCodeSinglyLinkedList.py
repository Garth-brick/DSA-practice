from typing import Any, Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __str__(self):
        return f"{self.val}"

    def print(self):
        # to print from a given listnode onwards
        curr: Optional[ListNode] = self
        while (curr):
            print(curr.val, end=" ")
            curr = curr.next
        print()

class LinkedList:
    def __init__(self, arr: Optional[list] = None):
        self.head: Optional[ListNode] = None
        self._size: int = 0

        if arr: 
            self.head = ListNode(arr[0])
            curr: Optional[ListNode] = self.head

            for i in arr[1:]:
                new_node = ListNode(i)
                curr.next = new_node
                curr = curr.next

            self._size = len(arr)
                
    def isEmpty(self):
        return self.head == None
    
    def print(self):
        curr: Optional[ListNode] = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        if (not self.head): return

        prevNode: Optional[ListNode] = None
        currNode: Optional[ListNode] = self.head
        while (currNode):
            nextNode: Optional[ListNode] = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode

    def size(self):
        return self._size