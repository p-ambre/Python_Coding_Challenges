"""

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                temp = node.right
                node.right = node.left
                node.left = temp
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return root
                
