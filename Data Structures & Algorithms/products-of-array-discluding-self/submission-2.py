class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        li = []
        for n in range(len(nums)):
            cur_sum = 1
            for x in range(len(nums)):
                if x == n:
                    continue
                cur_sum *= nums[x]
            li.append(cur_sum)
        return li
        '''
        res = [0] * len(nums)
        prefix = 1
        for n in range(len(nums)):
            res[n] = prefix
            prefix *= nums[n]
        postfix = 1
        for n in range(len(nums)-1, -1, -1):
            res[n] *= postfix
            postfix *= nums[n]
        return res
