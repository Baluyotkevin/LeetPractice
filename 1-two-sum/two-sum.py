class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we are going to iterate through the list
        # we create an object as we iterate to see if target is in the object
        # we save the remaining number to its index
        # we check to see if the remaining number is in the object
        # we return the indices if it is if not continue
        # assumption is that we always have a solution
        check = {}
        for i in range(len(nums)):
            # 9 - 2
            # remaining = 7
            remaining = target - nums[i]
            # 7 not in object
            if remaining not in check:
            # { 2 : 0 }

                check[nums[i]] = i
            elif remaining in check:
                return [i, check[remaining]]
            