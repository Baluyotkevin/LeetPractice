class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alphabet = {
            "a": "b",
            "b": "c",
            "c": "d",
            "d": "e",
            "e": "f",
            "f": "g",
            "g": "h",
            "h": "i",
            "i": "j",
            "j": "k",
            "k": "l",
            "l": "m",
            "m": "n",
            "n": "o",
            "o": "p", 
            "p":"q",
            "q": "r",
            "r":"s", 
            "s":"t", 
            "t": "u",
            "u": "v",
            "v": "w",
             "w":"x", 
             "x":"y", 
             "y": "z", 
             "z": "a"
            }

        j = 0
        for i in range(len(str1)):
            if j < len(str2):
                if str1[i] == str2[j] or alphabet[str1[i]] == str2[j]:
                    j += 1
        if j >= len(str2):
            return True
        else:
            return False

