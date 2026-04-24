class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sor = sorted(nums)
        num = 0
        max_count = 0
        cur_count = 0
        for n in range(1, len(nums)):
            if sor[n]-1 == sor[num]:
                num += 1
                cur_count += 1
            elif sor[n]-1 > sor[num]:
                num = n
                cur_count = 0
            else:
                num += 1  
            if cur_count > max_count:
                    max_count = cur_count
        return max_count + 1


                


