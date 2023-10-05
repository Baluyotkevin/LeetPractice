# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        check = float(inf)
        depth = 1
        stack = [[root, depth]]
        while stack:
            curr, currDepth = stack.pop()
            if curr.left:
                stack.append([curr.left, currDepth + 1])
            if curr.right:
                stack.append([curr.right, currDepth + 1])
            if not curr.left and not curr.right:
                check = min(check, currDepth)
        return check
                
        # return 1