class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_list[s[i]] < roman_list[s[i + 1]]:
                total -= roman_list[s[i]]
            else:
                total += roman_list[s[i]]
        return total
