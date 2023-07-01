from typing import Optional
from leetCodeSinglyLinkedList import ListNode, LinkedList

""" NOTES
- This is like mergine two lists with alternating elements
- Imagine if the input list was split along the middle into two lists
- Then you reverse all the links in the second half of the the list
- Get a pointer at the beginning of each list and start merging until one list finishes up

- You can use the fast and slow pointer method to find the middle of a linker list
"""

def reorderList(head: Optional[ListNode]) -> None:
    if not head: return
    
    # figuring out the midpoint of the list using fast and slow pointers
    slow, fast = head, head.next
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # just putting this in for typechecking sake
    if not slow: return

    # if the list has an odd number of elements then we are going to give the middle element to the left half
    # the first element of the right-half will be rightHead
    rightHead: Optional[ListNode] = slow.next

    # splitting the halves
    slow.next = None

    # reversing the right-half
    prevNode: Optional[ListNode] = None
    currNode: Optional[ListNode] = rightHead
    while(currNode):
        nextNode: Optional[ListNode] = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    rightHead = prevNode

    # merging the lists, one starts at 'head' and another starts at 'rightHead'
    while (head and rightHead):
        nextHead = head.next
        nextRightHead = rightHead.next
        head.next = rightHead
        rightHead.next = nextHead
        head = nextHead
        rightHead = nextRightHead