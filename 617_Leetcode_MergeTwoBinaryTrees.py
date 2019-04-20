"""

Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise, the NOT null
node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None or t2 is None:
            return t1 or t2
        else:
            root = t1
            stack = [(t1, t2)]
            while stack:
                t1, t2 = stack.pop()
                t1.val += t2.val
                if t1.left is None or t2.left is None:
                    t1.left = t1.left or t2.left
                else:
                    stack.append((t1.left, t2.left))
                if t1.right is None or t2.right is None:
                    t1.right = t1.right or t2.right
                else:
                    stack.append((t1.right, t2.right))
            return root
