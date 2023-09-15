class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        word = ""
        i = 0
        while i < length:
            word+=word1[i]
            word+=word2[i]
            i+=1
        word += word1[i:]
        word += word2[i:]
        return word