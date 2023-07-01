from typing import Optional, Dict

class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    if not head: return None

    # creating a map where all the old nodes correspond to their new nodes
    curr: Optional[Node] = head
    map: Dict[Node, Node] = {}
    while curr:
        map[curr] = Node(curr.val)
        curr = curr.next
    
    for oldNode, newNode in map.items():
        newNode.next = map[oldNode.next] if (oldNode.next) else None
        newNode.random = map[oldNode.random] if (oldNode.random) else None

    return map[head]