class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # we can just check whether the element is greater than its neighbors, if it is then append
        # since first and last cannot be peak we can just check in between which makes it easier for us to check neighbors
        peaks = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
