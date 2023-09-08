class Solution:
    def climbStairs(self, n: int) -> int:
        total_step = 1
        step2 = 0
        for i in range(1, n+1):
            step = total_step + step2
            step2 = total_step
            total_step = step
        
        return total_step
