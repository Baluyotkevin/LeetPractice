class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase_set = set([char for char in word if char == char.lower()])
        uppercase_set = set([char for char in word if char == char.upper()])
        count = 0
        for char in lowercase_set:
            if char.upper() in uppercase_set:
                count += 1
        return count