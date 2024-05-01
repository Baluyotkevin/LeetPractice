class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # sort so that we can identify the integer x
        # iterate through nums1 and find out the difference between all of them
        # should figure out the occurances
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]
  
