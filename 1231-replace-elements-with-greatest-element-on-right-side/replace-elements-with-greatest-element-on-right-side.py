class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = -1
        for i in range(len(arr) - 1, -1, -1):
            num_max = max(right, arr[i])
            arr[i] = right
            right = num_max
        return arr

