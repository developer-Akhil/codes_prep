# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Vedios : https://www.youtube.com/watch?v=hTM3phVI6YQ

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
Using Recursion 
"""

# class Solution():
#
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#Usin BSF

import collections as C

class Solution():
    def maxDepth(self,root:TreeNode)->int:
        if not root:
            return 0
        level = 0
        q=C.deque([root])

        print(q)
        while q:

            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            level +=1
        return level


# Using DFS

# class Solution():
#     def maxDepth(self,root:TreeNode)->int:
#
#         stack=[[root,1]]            # [[4,3]]
#         res=0                   #res=3
#
#         while stack:
#             node,depth = stack.pop()    #node=4 , depth=3
#
#             if node:                                # 5
#                 res = max(res,depth)                    # res = max(3,3)
#                 stack.append([node.left,depth+1])       # stack=[]
#                 stack.append([node.right, depth + 1])   # stack=[]
#
#         return res



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().maxDepth(root))

