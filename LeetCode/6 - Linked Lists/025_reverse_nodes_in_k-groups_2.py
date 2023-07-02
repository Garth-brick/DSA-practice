from typing import Optional
from leetCodeSinglyLinkedList import LinkedList, ListNode

def reverseList(head):
    prev = None
    curr = head
    while(curr):
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    lastSetNode = dummy
    for i in range(k):
        if not lastSetNode: break
        lastSetNode = lastSetNode.next
    # now LastSetNode will be pointing to the last node in the first set

    firstSetNode = head
    prevSetNode = dummy
    while lastSetNode:
        # if we don't have a last node in this set then we don't have to reverse it at all

        # storing the next node after this set is done
        nextSetNode = lastSetNode.next

        # reversing the list
        prevN = nextSetNode
        currN = firstSetNode
        for i in range(k):
            nextN = currN.next
            currN.next = prevN
            prevN = currN
            currN = nextN
        
        # connecting the ends of this list to the remaining list
        prevSetNode.next = prevN
        firstSetNode.next = nextSetNode

        # moving all the pointers to the next set
        prevSetNode = firstSetNode
        firstSetNode = nextSetNode
        lastSetNode = prevSetNode
        for i in range(k):
            if not lastSetNode: break
            lastSetNode = lastSetNode.next
    return dummy.next


list = LinkedList([1,2,3,4,5])
ln = reverseKGroup(list.head, 3)
if ln:
    ln.print()