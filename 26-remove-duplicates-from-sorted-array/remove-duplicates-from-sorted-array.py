class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        # compare = nums[0]
        length = 0
        while i < len(nums):
            compare = i - 1
            if nums[compare] != nums[i]:
                length += 1
                nums[length] = nums[i]
            i+=1
        return length + 1