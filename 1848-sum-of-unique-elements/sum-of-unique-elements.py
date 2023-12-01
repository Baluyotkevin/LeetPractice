class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        obj = defaultdict(int)

        for num in nums:
            obj[num] += 1

        return sum(value for value, count in obj.items() if count == 1)