class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for l in s:
            if l.isalnum():
                strs += l.lower()
        for n in range(len(strs) // 2):
            if strs[n] != strs[-n - 1]:
                return False
        return True
