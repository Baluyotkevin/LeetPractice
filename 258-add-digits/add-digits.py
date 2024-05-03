class Solution:
    def addDigits(self, num: int) -> int:
        num_string = str(num)
        while len(num_string) > 1:
            num_list = [ele for ele in num_string]
            num_string = str(sum([int(num) for num in num_list]))
        return int(num_string)