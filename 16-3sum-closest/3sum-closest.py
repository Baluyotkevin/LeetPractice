class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sum of three integers actually
        # iterate probalby two pointers so that we can check for each case
        # nbeed a variable to have a minimum to determine which is closest to the target
        # we need a variable to calculate the sum
        # we then iterate throguh all the numbers and then we return the minimum
        nums.sort()
        minDiff = float('inf')
        closestSum = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                totSum = nums[i] + nums[left] + nums[right]
                diff = abs(totSum - target)

                if diff < minDiff:
                    minDiff = diff
                    closestSum = totSum

                if totSum < target:
                    left += 1
                elif totSum > target:
                    right -= 1
                else:
                    return closestSum

        return closestSum


