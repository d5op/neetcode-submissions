class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        return list(sorted(dic.keys(), key=lambda x: dic[x], reverse=True))[:k]

