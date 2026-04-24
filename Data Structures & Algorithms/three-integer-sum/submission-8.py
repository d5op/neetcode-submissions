class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sor = sorted(nums)
        a = set()
        li = []
        for n in range(len(sor)):
            b, c = n + 1, len(sor) - 1
            while b < c:
                tol = sor[b] + sor[c] + sor[n]
                if tol < 0:
                    b += 1
                elif tol > 0:
                    c -= 1
                elif tol == 0 and tuple([sor[n],sor[b],sor[c]]) not in a:
                    li.append([sor[n],sor[b],sor[c]])
                    a.add(tuple([sor[n],sor[b],sor[c]]))
                    b += 1
                else:
                     b += 1
        return li
                    

