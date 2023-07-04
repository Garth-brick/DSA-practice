from typing import List
from leetCodeTree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count: List[int] = [0]

        def dfs(root: TreeNode, prevMax: int):
            if not root: return

            if root.val >= prevMax: 
                good_count[0] += 1
                prevMax = root.val
            
            dfs(root.left, prevMax)
            dfs(root.right, prevMax)

        dfs(root, root.val)
        return good_count[0]