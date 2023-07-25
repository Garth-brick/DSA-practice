from typing import Dict, List, Optional
import collections

class TreeNode:

    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def __init__(self, dataList: list = None) -> None:
        self.size: int = 0
        self.root: Optional[TreeNode] = None

        if dataList:
            self._createTreeFromList(dataList)
    

    def getParentIndex(self, i: int) -> int:
        return (i-1) // 2
    
    def getLeftChildIndex(self, i: int) -> int:
        return i*2 + 1

    def getRightChildIndex(self, i: int) -> int:
        return i*2 + 2


    def _createTreeFromList(self, dataList: list) -> None:
        if not dataList: return 

        # a map which will contain each index with its corresponding treenode
        map: Dict[int, TreeNode] = {}

        for i in range(len(dataList)):
            if not dataList[i]: continue
            map[i] = TreeNode(dataList[i])

        self.root = map[0]

        # now the map contains each index and its associated TreeNode
        # we will loop over all the nodes once again and connect them appropriately

        for i in range(len(dataList)):
            if not dataList[i]: continue

            l: int = self.getLeftChildIndex(i) 
            r: int = self.getRightChildIndex(i) 

            if l < len(dataList) and dataList[l]:
                # if the left child exists then add it
                map[i].left = map[l]
            if r < len(dataList) and dataList[r]:
                map[i].right = map[r]
        

    # left --> root --> right
    def inorderTraversal(self) -> None:
        stack: List[TreeNode] = []
        current: Optional[TreeNode] = self.root

        while True:

            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.val, end=" ")
                current = current.right
            else:
                break


    # root --> left --> right
    def preOrderTraversal(self) -> None:
        stack: List[TreeNode] = []
        current: Optional[TreeNode] = self.root

        while True:
            if current:
                print(current.val, end=" ")
                stack.append(current) # the stack will just store all the nodes whose right subtree hasn't been traversed yet. 
                current = current.left
            elif stack:
                current = stack.pop()
                current = current.right if current else None
            else:
                break
    
    # left --> right --> root
    def postOrderTraversal(self) -> None:
        return 
        # Some real fucky wucky backtracky shit is going downn here

        stack: List[TreeNode] = []
        current: Optional[TreeNode] = self.root

        while True:

            if current:
                stack.append(current)
                current = current.left
            elif stack:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    print(temp.val)
                current = stack.pop()
                current = current.right
            else:
                break


    # top to bottom, left to right on the same level
    def levelOrderTraversal(self) -> None:

        queue = collections.deque()
        queue.append(self.root)

        while queue:
            node: Optional[TreeNode] = queue.popleft()
            if not node: continue

            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)


# TESTING

# t1 represents this tree
#       4
#     /   \
#    2     6
#   / \   / \
#  1   3 5   7

# t1 = Tree([4,2,6,1,3,5,7])
# t1.inorderTraversal()
# print()
# t1.postOrderTraversal()