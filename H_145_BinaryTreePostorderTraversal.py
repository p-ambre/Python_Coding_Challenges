"""

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

ALGORITHM:
1.1 Create an empty stack
2.1 Do following while root is not NULL
    a) Push root's right child and then root to stack.
    b) Set root as root's left child.
2.2 Pop an item from stack and set it as root.
    a) If the popped item has a right child and the right child
       is at top of stack, then remove the right child from stack,
       push the root back and set root as root's right child.
    b) Else print root's data and set root as NULL.
2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

POSTORDER: (left, right, root)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def peek(self, stack):
        if len(stack) > 0:
            return(stack[-1])
        return None

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack = []
        ans = []

        while(True):
            while(root):
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            if (root.right is not None and self.peek(stack) == root.right):
                stack.pop()
                stack.append(root)
                root = root.right

            else:
                ans.append(root.val)
                root = None

            if len(stack) <= 0:
                return ans
