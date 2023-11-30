class Solution:
    def sortSentence(self, s: str) -> str:
        lis = s.split(' ')
        ans = [0] * len(lis)
        for i in range(len(lis)):
            idx = int(lis[i][-1])
            word = lis[i][0:-1]
            ans[idx - 1] = word
        return ' '.join(ans)
        # words = {}
        # ans = []
        # temp = 0
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i].isdigit():
        #         temp = s[i]
        #         words[s[i]] = ''
        #     elif s[i].isalpha():
        #         words[temp] = s[i] + words[temp]
        # word_sort = sorted(words.items())
        # for j in range(len(word_sort)):
        #     ans.append(word_sort[j][1])
        # return ' '.join(ans)