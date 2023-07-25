""" NOTES, FIRST APPROACH
- We'll first traverse the BST to find p and mark all the TreeNodes on the way as "ancestors" 
- Then we'll start traversing the BST to find q and keep checking if the TreeNode we are currently at is an ancestor of p too. 
    - If it is an ancestor of p then we'll update our LCA node. If 
    - If it isn't an ancestor of p then we'll return our LCA node

SECOND APPROACH
- Traverse the tree to find both p and q simultaneously until you need to look for them separately
- So if both are lesser than the root, then move left, if both are greater then move right
- Return the root if one value is equal to the root, or if one is lesser and one is greater
"""

from leetCodeTree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val == p.val or root.val == q.val): return root
        if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val): return root
        if (p.val < root.val and q.val < root.val): return self.lowestCommonAncestor(root.left, p, q)
        if (p.val > root.val and q.val > root.val): return self.lowestCommonAncestor(root.right, p, q)