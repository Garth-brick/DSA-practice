from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while (curr):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def printList(head: Optional[ListNode]) -> None:
    curr = head
    while(curr):
        print(curr.val)
        curr = curr.next

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
printList(reverseList(l1))