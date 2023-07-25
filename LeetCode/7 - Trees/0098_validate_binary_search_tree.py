""" NOTES
- The value of each node should lie within a range, just make sure to set that range properly for each node
- If we are checking on the left side then the upper limit should be kept in check because we want all nodes on the left to be lesser (i.e. below that upper limit)
- If we are checking on the right side then the lower limit should be kept in check because we want all the nodes on the right side to be greater (i.e above that lower limit)
"""

import math
from typing import Optional

from leetCodeTree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode], lowerLimit=-math.inf, upperLimit=math.inf) -> bool:
        if not root: return True

        if not (root.val < upperLimit and root.val > lowerLimit): return False

        leftValid = self.isValidBST(root.left, lowerLimit, min(upperLimit, root.val))
        rightValid = self.isValidBST(root.right, max(lowerLimit, root.val), upperLimit)
        return  leftValid and rightValid