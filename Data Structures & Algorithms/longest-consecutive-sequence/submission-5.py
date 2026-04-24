class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = maxlen = 0
        numSet = set(nums)
        for n in nums:
            if n-1 not in numSet:
                length = 0
                while n+length in numSet:
                    length += 1
            maxlen = max(maxlen, length)
        return maxlen

                


