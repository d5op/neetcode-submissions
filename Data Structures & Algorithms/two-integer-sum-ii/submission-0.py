class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for n in range(len(numbers)):
            com = target - numbers[n]
            if numbers[n] in dic:
                return [dic[numbers[n]], n+1]
            else:
                dic[com] = n+1