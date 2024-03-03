class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        string = n
        while string != 1 and string not in seen:
            seen.add(string)
            string = sum([int(num)**2 for num in str(string)])
        return True if string == 1 else False
                
                