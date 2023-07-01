from typing import Optional
from leetCodeSinglyLinkedList import ListNode, LinkedList


# this doesn't work specifically when the size is 2 and tail is to be removed because the slow pointer ends up remaining on the head and then that leads to it removing the head itself
# to get around it we'll have to use a dummy node as the beginning of our list


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if (not head) or (not head.next) or (n <= 0):
        return None
    
    # I'll start both pointers at the head, then move the fast pointer forward by n nodes
    fast: Optional[ListNode] = head
    slow: Optional[ListNode] = head
    for i in range(n):
        if fast: 
            fast = fast.next
    # now the fast pointer should be at the (n+1)th node
    # now we move both the pointers together until the fact pointer reaches the last node, i.e. until the fast pointer doesn't have a next node
    while slow and fast and fast.next:
        # checking for the existence of 'slow' and 'fast' as well for typechecking purposes
        slow = slow.next
        fast = fast.next
    
    # now the slow pointer should be just before the node that we want to remove

    # if it is still at the head then we need to remove the head itself
    if slow == head:
        head = head.next

    if slow and slow.next:
        slow.next = slow.next.next

    return head

l = LinkedList([1,2])
ln1 = removeNthFromEnd(l.head, 2)
if ln1:
    ln1.print()