class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            steps = f"{nums[i]}"
            count = 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1] - 1:
                count += 1
                i += 1
            if count != 1:
                steps += "->" + f"{nums[i]}"
            ans.append(steps)
            i += 1
        return ans
