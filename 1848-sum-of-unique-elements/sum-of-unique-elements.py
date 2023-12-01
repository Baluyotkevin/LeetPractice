class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        obj = {}
        for num in nums:
            if num not in obj: 
                obj[num] = 1
            else:
                obj[num] += 1
        return sum(value for value, count in obj.items() if count == 1)