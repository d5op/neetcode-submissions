class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        return list(sorted(dic.keys(), key=lambda x: dic[x], reverse=True))[:k]

