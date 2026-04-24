class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for l in s:
            if l.isalnum():
                strs += l.lower()
        return strs == strs[::-1]
