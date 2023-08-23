class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dictionary
        # nums will be keys
        # values will be how many times it has appeared
        # return value = 1
        vanessa = {}
        for num in nums:
            # print(vanessa[num])
            if num not in vanessa.keys():
                vanessa[num] = 1
            else:
                vanessa[num]+=1

        for key, val in vanessa.items():
            if val == 1:
                return key