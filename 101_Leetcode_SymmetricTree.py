"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, root1, root2):
        if (root1 is None and root2 is None):
            return True
        if(root1 is not None and root2 is not None):
            if root1.val == root2.val:
                return(self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))

        return False


    def isSymmetric(self, root: TreeNode) -> bool:
        return(self.isMirror(root, root))
