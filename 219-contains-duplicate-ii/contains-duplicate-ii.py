class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        new = {}
        for i in range(len(nums)):
            if nums[i] in new and k >= abs(i - new[nums[i]]):
                return True
            new[nums[i]] = i
        return False

                