class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            index = nums2.index(num)
            for j in range(index, len(nums2)):
                if nums2[j] > num:
                    ans.append(nums2[j])
                    break
                elif j == len(nums2) - 1 and num >= nums2[j]:
                    ans.append(-1)
        return ans
