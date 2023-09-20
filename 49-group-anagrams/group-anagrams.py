class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for word in strs:
            key = "".join((sorted(word)))
            if key not in answer:
                answer[key] = [word]
            else:
                answer[key].extend([word])
        return answer.values()