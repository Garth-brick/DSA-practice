from typing import Optional
from leetCodeTree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = False
        if (not p and q) or (p and not q): return False
        if (not p and not q): return True

        result = p.val==q.val
        leftSame = self.isSameTree(p.left, q.left)
        rightSame = self.isSameTree(p.right, q.right)
        return leftSame and rightSame and result