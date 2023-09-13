# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        stack = [p]
        stack_two = [q]
        while stack:
            curr = stack.pop()
            curr_two = stack_two.pop()
            if curr.val != curr_two.val:
                return False
            if curr.left is None and curr_two.left or curr.right is None and curr_two.right or curr_two.left is None and curr.left or curr_two.right is None and curr.right:
                return False
            if curr.left and curr_two.left:
                stack.append(curr.left)
                stack_two.append(curr_two.left)
            if curr.right and curr_two.right:
                stack.append(curr.right)
                stack_two.append(curr_two.right)
        return True