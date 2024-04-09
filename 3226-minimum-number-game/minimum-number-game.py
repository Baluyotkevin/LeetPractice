class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # can do recursion
        # can return when array nums is empty
        # once you find minimum you pop it
        # call function after you pop elemetn from arr
        if len(nums) == 0:
            return []
        min_num = min(nums)
        index = nums.index(min_num)
        nums.pop(index)
        min_num_two = min(nums)
        index_two = nums.index(min_num_two)
        nums.pop(index_two)
        return [min_num_two, min_num] + self.numberGame(nums)