class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[]]
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
            freq.append([])
        for key,v in dic.items():
            freq[v].append(key)
        res = []
        for n in range(len(freq)-1, 0, -1):
            for w in freq[n]:
                res.append(w)
                if len(res) == k:
                    return res

