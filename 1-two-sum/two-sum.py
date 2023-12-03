class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            tot = target - nums[i]
            if tot in check:
                return [i, check[tot]]
            else:
                check[nums[i]] = i