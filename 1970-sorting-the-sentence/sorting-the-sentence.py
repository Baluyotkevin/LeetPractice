class Solution:
    def sortSentence(self, s: str) -> str:
        lis = s.split(' ')
        ans = [0] * len(lis)
        for i in range(len(lis)):
            idx = int(lis[i][-1])
            word = lis[i][0:-1]
            ans[idx - 1] = word
        return ' '.join(ans)