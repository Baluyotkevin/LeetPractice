# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return true
        def isSym(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None or left.val != right.val:
                return False
            return isSym(left.left, right.right) and isSym(left.right, right.left)
        return isSym(root.left, root.right)