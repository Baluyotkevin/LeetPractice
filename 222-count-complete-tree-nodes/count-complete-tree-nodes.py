# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left_count = dfs(node.left)
            right_count = dfs(node.right)
            return 1 + left_count + right_count
        return dfs(root)