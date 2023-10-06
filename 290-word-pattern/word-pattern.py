class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        check = {}
        look = s.split()
        if len(set(pattern)) != len(set(look)):
            return False
        if len(pattern) != len(look):
            return False
        for i in range(len(look)):
            if pattern[i] not in check:
                check[pattern[i]] = look[i]
            elif check[pattern[i]] == look[i]:
                continue
            else:
                return False
        return True

                