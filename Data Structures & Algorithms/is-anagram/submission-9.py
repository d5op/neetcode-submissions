class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for w in s:
            dic[w] = dic.get(w, 0) + 1
        for w in t:
            if w not in dic or dic[w] < 1:
                return False
            else:
                dic[w] -= 1
        return True