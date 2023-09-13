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
            # root = [3, 1]
            curr_node, curr_level = stack.pop()
            # curr_node = [9, 2]
            # curr_node = [20, 2]
            # curr_node = [15, 3]
            if curr_node is None: continue
            # stack = [[curr_node.left = 9, 2]]
            # stack = [[curr_node.right = 20, 2]]
            # stack = [] it is currently empty
            # does curr_node have a left or right? no so move onto the next
            # does curr_node have a left or right?
            # does curr_node have a left or right?
            stack.append([curr_node.left, curr_level + 1])
            # stack = [[curr_node.left = 9, 2], [curr_node.right = 20, 2]]
            # yes it has a left so add to stack stack = [[15, 3]]
            # no
            stack.append([curr_node.right, curr_level + 1])
            # yes it has a right so add to stack = [[15, 3], [7, 3]]
            # no
            max_level = max(max_level, curr_level)
            # max_level = (1, 2)
            # max_level = 2
            # max_level = (2, 2)
            # max_level = 2
            # max_level = (2, 3)
            # max_level = 3
            # max_level (3, 3)
            # max_level = 3
        # return 3 if root is not undefined otherwise if it is return 0
        return max_level if root is not None else 0