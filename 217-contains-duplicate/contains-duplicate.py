class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = {}
        for num in nums:
            if num not in new:
                new[num] = 1
            else:
                new[num] += 1
        for key, value in new.items():
            if value > 1:
                return True
        return False