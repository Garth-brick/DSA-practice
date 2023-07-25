from typing import Optional
from leetCodeSinglyLinkedList import ListNode, LinkedList

# this works but it's too slow

def reorderList(head: Optional[ListNode]) -> None:
    if not head:
        return
    curr: Optional[ListNode] = head
    while curr:
        prevLastNode: ListNode = curr
        lastNode: ListNode = curr
        while lastNode.next:
            # this will keep going on until there is no next node after lastNode
            prevLastNode = lastNode
            lastNode = lastNode.next
        prevLastNode.next = None

        nextNode: Optional[ListNode] = curr.next
        curr.next = lastNode
        lastNode.next = nextNode
        curr = nextNode

list1 = LinkedList([1,2,3,4])
reorderList(list1.head)
list1.print()