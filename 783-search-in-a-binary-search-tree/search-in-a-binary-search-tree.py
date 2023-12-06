# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return root
        stack = [root]
        while len(stack):
            curr = stack.pop()
            if curr and curr.val == val:
                return curr
            if curr and curr.left:
                stack.append(curr.left)
            if curr and curr.right:
                stack.append(curr.right)
        return None