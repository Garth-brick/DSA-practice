from typing import Optional
from leetCodeSinglyLinkedList import LinkedList, ListNode

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
    # making a dummy node the head of the linked list
    dummy: ListNode = ListNode(val=-1, next=head)

    slow: ListNode = dummy
    fast: ListNode = dummy
    for i in range(n):
        if fast and fast.next:
            fast = fast.next
    # now the fast pointer will be n nodes ahead of the slow pointer so we start moving them together
    while slow and slow.next and fast and fast.next:
        # added slow and slow.next to the while loop for type-checking
        slow = slow.next
        fast = fast.next

    # now slow should be right behind the node that it has to remove
    if slow and slow.next:
        # detaching the link from the removed node and storing its next node
        nextNode = slow.next.next
        slow.next.next = None

        # re-attaching the nextNode to the list
        slow.next = nextNode
    
    return dummy.next

l = LinkedList([1,2])
ln1 = removeNthFromEnd(l.head, 2)
if ln1:
    ln1.print()