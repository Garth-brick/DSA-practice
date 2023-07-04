from typing import Optional
from leetCodeTree import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if (p and not q) or (not p and q): return False
        if (not p and not q): return True
        if (not p.val==q.val): return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        
        if root.val==subRoot.val and self.isSameTree(root, subRoot): return True
           
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)