"""

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

ALGORITHM:
1) Create an empty stack nodeStack and push root node to stack.
2) Do following while nodeStack is not empty.
….a) Pop an item from stack and print it.
….b) Push right child of popped item to stack
….c) Push left child of popped item to stack

INORDER: (Left, Root, Right----LRoR)
PREORDER: (Root, Left, Right---RoLR)
POSTORDER: (Left, Right, Root----LRRo)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_stack = []
        preorder = []
        if root is None:
            return []
        node_stack.append(root)

        while(len(node_stack) > 0):
            root_node = node_stack.pop()
            preorder.append(root_node.val)

            if root_node.right is not None:
                node_stack.append(root_node.right)
            if root_node.left is not None:
                node_stack.append(root_node.left)
        return preorder
