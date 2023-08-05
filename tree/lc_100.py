# Definition for a  binary tree node
from typing import Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self,p : Optional[TreeNode], q: Optional[TreeNode]):

        if not p and not q:         # if both are null then it will return true
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


root1 = TreeNode(1)
root2 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)


if Solution().isSameTree(root1, root2):
    print("Both trees are identical")
else:
    print ("Trees are not identical")

# for a,b in zip(a,b):
#     print(Solution().isSameTree(a, b))



