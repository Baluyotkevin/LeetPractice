class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ""
        for i in range(len(digits)):
            digit += str(digits[i])
        new = int(digit) + 1
        return [int(ele) for ele in str(new)]
