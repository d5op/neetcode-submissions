class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute
        '''
        li = [[strs[0]]]
        alr_app = False
        for w in range(1,len(strs)):
            for x in range(len(li)):
                if Counter(strs[w]) == Counter(li[x][0]):
                    li[x].append(strs[w])
                    alr_app = True
                    break
            if not alr_app:
                li.append([strs[w]])
            alr_app = False
        li.sort(key=len, reverse=True)
        return li
        '''
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