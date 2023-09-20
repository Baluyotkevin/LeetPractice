class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # reset check back to 0 each time its count >= 2
        # append if count is >= 2
        # return
        answer = []
        check = {}
        for el in nums:
            if el not in check:
                check[el] = 1
            else:
                check[el] += 1
        lis = []
        for num in check.values():
            lis.append(num)
        lis.sort()
        lis = lis[-k:]
        for i in lis:
            for k in check:
                if check[k] == i and k not in answer:
                    answer.append(k)
        return answer

