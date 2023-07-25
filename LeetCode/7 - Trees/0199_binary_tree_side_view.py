""" NOTES
- The plan is to create the same level order traversal queue but keep picking the right-most element first and adding it to the result before going over the rest of the elements as usual
"""
import collections
from typing import List, Optional
from leetCodeTree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        q: collections.deque[TreeNode] = collections.deque()

        if not root: return []
        q.append(root)

        while q:
            rightNode = q[-1] # grabbing the rightmost element and adding it the result
            result.append(rightNode.val)

            # now going over every element currently in the queue (which is all the elements at this level) while adding its children to the back of the queue
            qLengthAtStart = len(q)
            for i in range(qLengthAtStart):
                node = q.popleft()
                if not node: continue
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return result