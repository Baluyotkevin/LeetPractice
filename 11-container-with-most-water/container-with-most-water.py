class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer where we have
        # left pointer and right pointer max num()
        # variable to keep track of length because we want the max length we can get but also the highest height
        # we would keep track of the max(area)
        # left <= right
        l, r = 0, len(height) - 1
        max_area = float('-inf')
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
            