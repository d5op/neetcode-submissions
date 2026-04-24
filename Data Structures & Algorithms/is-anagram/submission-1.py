class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for n in s:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for n in t:
            if n not in dic or dic[n] == 0:
                return False
            else:
                dic[n] -= 1
        return True