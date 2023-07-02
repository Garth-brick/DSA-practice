from typing import Optional
from leetCodeSinglyLinkedList import ListNode, LinkedList


# good attempt but I do not know why this doesn't work :/


""" NOTES 
My approach:
- Keep a pointer that jumps from one set to the other set and another pointer that is responsible for all the reversing
- Reverse a set of nodes
    - Keep in mind to connect the reversed set of nodes to the remaining list
    - The last node in a set should be connected the the node before the set
    - The first node in a set should be connected to the node after the set
"""
def reverseList(head: Optional[ListNode], prev: Optional[ListNode], n: int, next: Optional[ListNode] = None) -> Optional[ListNode]:
    if (not head) or not (head.next): return

    prevNode = next # so that the node that is first right now ends up pointing the node that is next later 
    currNode = head
    for i in range(n):
        if not currNode: break

        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode

    if prev:
        prev.next = currNode # so that the node has become the new head is pointed to by the last node from the previous set
    return currNode


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy: ListNode = ListNode(0, head)

    # lets send out a pointer that is n nodes ahead so that we can easily grab the first element from the next set and so that we can check whether we even need to do any reversing in the first place
    nextSetPrev: Optional[ListNode] = dummy
    for i in range(k):
        # if we can't even move this pointer n nodes then there is no reversing needed at all
        if not nextSetPrev: return head

        nextSetPrev = nextSetPrev.next
    
    currSetPrev: ListNode = dummy
    
    while nextSetPrev:
        reverseList(currSetPrev.next, currSetPrev, k, nextSetPrev.next)
        currSetPrev = nextSetPrev
        for i in range(k):
            if not nextSetPrev: break
            nextSetPrev = nextSetPrev.next
    
    return dummy.next
