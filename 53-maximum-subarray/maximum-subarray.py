class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            max_sub = max(max_sub, currSum)
        return max_sub