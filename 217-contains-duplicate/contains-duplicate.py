class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for num in nums:
            if num not in check:
                check[num] = 1
            else:
                check[num] += 1
        for quantity in check.values():
            if quantity > 1:
                return True
        return False