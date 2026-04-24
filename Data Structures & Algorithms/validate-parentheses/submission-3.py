class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        for n in s:
            if n in pair:
                stack.append(pair[n])
            else:
                if len(stack) < 1 or stack.pop() != n:
                    return False
        return len(stack) == 0