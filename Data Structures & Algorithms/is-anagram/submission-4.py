class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for n in s:
            dic[n] = dic.get(n, 0) + 1
        for n in t:
            if n in dic and dic.get(n) > 0:
                dic[n] = dic.get(n) - 1
            else:
                return False
            
        return True
            