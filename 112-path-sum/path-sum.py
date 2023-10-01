# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if not root: return False
        # if not root.left and not root.right and targetSum == root.val:
        #     return True
        # return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)          
        if not root: return False
        stack = [[root, root.val]]
        while stack:
            curr, currVal = stack.pop()
            if currVal == targetSum and not curr.left and not curr.right: return True
            if curr.right: stack.append([curr.right, currVal + curr.right.val])
            if curr.left: stack.append([curr.left, currVal + curr.left.val])
            
        return False



                
