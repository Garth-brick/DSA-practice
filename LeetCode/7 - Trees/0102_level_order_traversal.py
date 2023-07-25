""" NOTES
- We need perform a bfs on this tree
- Create a queue and add the root node to it
- while the queue is not empty, pop all the elements in the queue while adding their children to the queue
- To make sure that the result list is segregated by levels, while you are iterating over the queue, make sure to store how many nodes are present in the queue at a given level first and then only pop that many nodes ()while adding their children to the back of the queue). 
"""

import collections
from typing import List, Optional

from leetCodeTree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q: collections.deque[TreeNode] = collections.deque()
        q.append(root)

        while q:
            level = []
            qLengthAtStart = len(q)
            # storing the current length of the queue before beginning to pop nodes is imporant because we want our result list to be segregated by levels. Only popping all nodes present in the queue at the start ensures that we don't add any of their children to the sublist for this level (because their children will be added in right as they are popped)
            for i in range(qLengthAtStart):
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level: 
                result.append(level)
        
        return result