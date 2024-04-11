class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # we can iterate through the array
        # count and iterate at the same time
        # we can check if in array count += 1
        # i dont htink we can do it at the same time actually because length varies
        count = 0
        count_two = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count += 1
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                count_two += 1
        return [count, count_two]