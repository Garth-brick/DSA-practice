from typing import Optional
from leetCodeTree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0