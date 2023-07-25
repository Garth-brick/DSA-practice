from typing import Optional, List
from leetCodeSinglyLinkedList import ListNode


""" NOTES
- My intuitive approach involved using a heap to store the first node of each list, then pop the minimum, add the minimum to the result list, and add the next element to the heap (from the list we just popped) and then just continue.

- Actual solution is kinda like mergesort
- Merge pairs of nodes to make a linked list of two nodes --> merge these lists togther again and again until you just have a single list
- If we have n elements and k lists then 
    - We take O(n) to merge two sorted linked lists
    - We are going to performing this merge operation log(k) times 
    - Time Complexity = O(n log(k))
"""

def mergeList(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # merging two sorted lists
    dummy: ListNode = ListNode()
    curr: Optional[ListNode] = dummy
    while (list1 and list2):
        if (list1.val <= list2.val):
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1:
        curr.next = list1
    else:
        curr.next = list2
    return dummy.next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or not len(lists): return None

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1: Optional[ListNode] = lists[i] if (i < len(lists)) else None
            l2: Optional[ListNode] = lists[i+1] if (i+1 < len(lists)) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]
