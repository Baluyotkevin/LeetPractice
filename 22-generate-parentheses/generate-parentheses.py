class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dps(combo, memo, left, right):
            if left == 0 and right == 0:
                memo.append(combo)
            if left > 0:
                dps(combo + '(', memo, left - 1, right)
            if left < right:
                dps(combo + ')', memo, left, right - 1)
            

        memo = []
        dps('', memo, n, n)
        return memo