class Solution:
    def addDigits(self, num: int) -> int:
        sum_num = 0
        while num > 9:
            num = str(num)
            num = [int(numb) for numb in num]
            num = sum(num)
        return num