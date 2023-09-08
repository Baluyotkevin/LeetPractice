class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        max_sum = 0
        """
        want to find max sum
        if lp == rp lp++ and do not add
        """
        lp = 0
        rp = len(mat) - 1
        i = 0
        while len(mat) > i:
            if lp != rp:
                max_sum += mat[i][lp]
            max_sum += mat[i][rp]
            lp+=1
            rp-=1
            i+=1
        return max_sum