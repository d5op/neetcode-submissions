class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for n in range(len(nums)):
            com = target - nums[n]
            if com in dic and n != dic[com]:
                return [dic[com], n]
            else:
                dic[nums[n]] = n
