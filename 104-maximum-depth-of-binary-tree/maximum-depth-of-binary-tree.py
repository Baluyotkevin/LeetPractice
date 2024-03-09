# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_level = 1
        stack = [[root, max_level]]
        while stack:
            curr, lvl = stack.pop()
            max_level = max(lvl, max_level)
            if curr.left:
                stack.append([curr.left, lvl + 1])
            if curr.right:
                stack.append([curr.right, lvl + 1])
        return max_level