from typing import Optional
from leetCodeSinglyLinkedList import LinkedList, ListNode

def hasCycle(head: Optional[ListNode]) -> bool:
    if not head: return False

    fast: Optional[ListNode] = head.next
    slow: Optional[ListNode] = head

    while slow and fast:
        if (fast is slow):
            return True
        fast = fast.next.next if fast.next else None
        slow = slow.next
    return False