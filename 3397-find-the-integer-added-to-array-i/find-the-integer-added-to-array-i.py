class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # sort so that we can identify the integer x
        # iterate through nums1 and find out the difference between all of them
        # should figure out the occurances
        obj = {}
        nums1.sort()
        nums2.sort()
        total = 0
        for i in range(len(nums1)):
            diff = nums2[i] - nums1[i]
            total = diff
            if diff not in obj:
                obj[diff] = 1
            else:
                obj[diff] += 1
            return total
            
