class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        while i < 2:
            for num in nums:
                answer.append(num)
            i += 1
        return answer
        # for el in answer.split():
        #     nums.append(int(el))
        # return answer
            