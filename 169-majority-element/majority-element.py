class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        obj = {}
        for i in range(len(nums)):
            if nums[i] not in obj:
                obj[nums[i]] = 1
            else:
                obj[nums[i]] += 1
        m = 0
        for key, value in obj.items():
            m = max(m, value)
        for key, value in obj.items():
            if value == m:
                return key            
        return 0