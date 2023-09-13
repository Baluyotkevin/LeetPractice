# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_level, stack = 1, [[root, 1]]
        while stack:
            curr_node, curr_level = stack.pop()
            if curr_node is None: continue
            stack.append([curr_node.left, curr_level + 1])
            stack.append([curr_node.right, curr_level + 1])
            max_level = max(max_level, curr_level)
        return max_level if root is not None else 0