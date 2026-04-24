class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li = []
        for n in range(len(nums)):
            cur_sum = 1
            for x in range(len(nums)):
                if x == n:
                    continue
                cur_sum *= nums[x]
            li.append(cur_sum)
        return li

