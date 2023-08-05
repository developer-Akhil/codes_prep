# Theory -> https://favtutor.com/blogs/invert-binary-tree
# Vedio -> https://www.youtube.com/watch?v=vRbbcKXCxOw

from typing import Optional
class TreeNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def PrintTree ( self ) :
       if self.left :
           self.left.PrintTree ()
       print ( self.data, end= ' ' ) ,
       if self.right :
           self.right.PrintTree ()

class Solution:
    '''
    Function to invert the tree
    '''
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


if __name__ == '__main__':
    '''
                10                                              10
              /    \                                          /    \           
            20      30              ========>>              30      20           
           /         \                                      /        \
          40          50                                  50          40 
    '''
    Tree = TreeNode(10)
    Tree.left = TreeNode(20)
    Tree.right = TreeNode(30)
    Tree.left.left = TreeNode(40)
    Tree.right.right = TreeNode(50)
    print('Initial Tree :',end = ' ' )
    Tree.PrintTree()
    Solution().invertTree(root=Tree)
    print('\nInverted Tree :', end=' ')
    Tree.PrintTree()