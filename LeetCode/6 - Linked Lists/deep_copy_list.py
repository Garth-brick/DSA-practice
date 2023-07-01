from typing import Optional, Dict
from leetCodeSinglyLinkedList import ListNode as Node, LinkedList


def copyList(head: Optional[Node]) -> Optional[Node]:
    if not head: return None

    # using a map to store every original node with its associated next node
    map: Dict[Node, Node] = {}
    curr: Optional[Node] = head

    while curr:
        map[curr] = Node(curr.val)
        curr = curr.next
    
    for oldNode, newNode in map.items():
        newNode.next = map[oldNode.next] if (oldNode.next) else None
    
    return map[head]


ll= LinkedList([1,2,3,4])
ln: Optional[Node] = copyList(ll.head)
if ll.head:
    ll.head.val = 5
ll.print()
if ln:
    ln.print()