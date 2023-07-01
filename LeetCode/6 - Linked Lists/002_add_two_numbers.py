from typing import Optional
from leetCodeSinglyLinkedList import ListNode, LinkedList


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # just creating a reault list with a dummy head
    resultHead: ListNode = ListNode()

    curr: ListNode = resultHead

    carry: int = 0
    while (l1 or l2):
        val1: int = l1.val if (l1) else 0
        val2: int = l2.val if (l2) else 0
        sum: int =  val1 + val2 + carry
        carry = sum // 10
        sum = sum % 10
        curr.next = ListNode(sum)
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        curr = curr.next
    if carry:
        curr.next = ListNode(carry)
    
    return resultHead.next

l1 = LinkedList([9,9,9,9,9,9,9])
l2 = LinkedList([9,9,9,9])
ln = addTwoNumbers(l1.head, l2.head)
if ln: ln.print()