from typing import Optional
from leetCodeTree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        left = root.left
        root.left = root.right
        root.right = left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root