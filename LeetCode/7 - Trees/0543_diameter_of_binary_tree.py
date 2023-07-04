from typing import Optional
from leetCodeTree import TreeNode


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root: TreeNode):
            if not root: return 0

            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            result[0] = max(result[0], leftDepth + rightDepth)
            return max(leftDepth, rightDepth) + 1

        dfs(root)

        return result[0]
