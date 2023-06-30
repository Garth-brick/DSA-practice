from typing import Any, List, Optional
from leetCodeSinglyLinkedList import ListNode, LinkedList

# we can't create copies of the nodes

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy: ListNode = ListNode(-1)
    tail: ListNode = dummy
    while list1 and list2:
        if (list1.val < list2.val):
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next

list1 = LinkedList([1,2,4])
list2 = LinkedList([1,3,4])
ln1 = mergeTwoLists(list1.head, list2.head)
if ln1:
    ln1.print()
