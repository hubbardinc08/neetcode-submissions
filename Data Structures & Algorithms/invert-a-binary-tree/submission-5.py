# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = deque()
        tree.append(root)

        while len(tree) > 0:
            curr_node = tree.popleft()
            if (curr_node is not None):
                left = curr_node.left
                curr_node.left = curr_node.right
                curr_node.right = left

                tree.append(curr_node.left)
                tree.append(curr_node.right)
        
        return root
