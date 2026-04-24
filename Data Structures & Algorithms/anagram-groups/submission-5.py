class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #opt1
        s = {}
        li = []
        for n in range(len(strs)):
            tup = tuple(sorted(Counter(strs[n]).items()))
            if tup not in s:
                s[tup] = len(s)
                li.append([strs[n]])
            else:
                li[s[tup]].append(strs[n])
        li.sort(key=len, reverse=True)
        return li