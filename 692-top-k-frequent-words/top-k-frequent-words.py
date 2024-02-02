class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # dictionary word and frequency values
        # iterate through list
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        sort = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        ans = []
        i = 0
        while i < k:
            ans.append(sort[i][0])
            i += 1
        return ans


        # arr = []
        # for k, v in dic.items():
        #     arr.append([k, v])
        # sorted(arr, key=)
            