class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        string = n
        while string != 1 and string not in seen:
            seen.add(string)
            string = str(string)
            tot = 0
            for i in range(len(string)):
                tot += int(string[i])**2
            string = tot
        return True if string == 1 else False
                
                