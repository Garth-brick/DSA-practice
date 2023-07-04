from typing import Optional
from leetCodeTree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def dfs(root):
            if not root: return 0
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            if abs(leftDepth-rightDepth) > 1: 
                result[0] = False
            return max(leftDepth, rightDepth) + 1

        dfs(root)

        return result[0]