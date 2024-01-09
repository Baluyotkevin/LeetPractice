class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        test_case = -2**31
        test_case2 = 2**31 - 1
        if x < 0:
            is_negative = True
            x = abs(x)
        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str)
        if reversed_int > test_case2 or reversed_int < test_case:
            return 0
        return -reversed_int if is_negative else reversed_int

