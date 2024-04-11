class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        contains = []
        for i in range(len(words)):
            if x in words[i]:
                contains.append(i)
        return contains
