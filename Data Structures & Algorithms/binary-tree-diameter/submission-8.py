# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        x = 0

        def calc(root):
            nonlocal x
            if (root is None):
                return 0
            
            left = calc(root.left)
            right = calc(root.right)

            x = max(x, left + right)

            return 1 + max(left, right)
        
        calc(root)
        return x