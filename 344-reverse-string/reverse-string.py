class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # index = len(s) - 1
        # for i in range(len(s)):  
        #     temp = s[i]
        #     s[i] = s[index]
        #     s[index] = temp
        #     index -= 1
        #     if index <= i:
        #         break
        left = 0
        right = len(s) - 1
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s
