class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # we want to check each string maybe its length
        # check to see if the left equals each other or if any of them equal each other
        # maximum operations is 3 because you can only delete 1 from each str
        # we want to iterate through each string to check
        lengths = [len(s1), len(s2), len(s3)]
        min_length = min(lengths)
        count = 0
        for i in range(min_length):
            if s1[i] == s2[i] and s1[i] == s3[i]:
                count += 1
            else:
                break
        if count == 0:
            return -1
        res = sum(length - count for length in lengths)
        return res