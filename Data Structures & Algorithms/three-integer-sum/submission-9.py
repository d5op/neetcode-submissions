class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sor = sorted(nums)
        li = []
        for n in range(len(sor)):
            if n > 0 and sor[n] ==sor[n - 1]:
                continue
            b, c = n + 1, len(sor) - 1
            while b < c:
                tol = sor[b] + sor[c] + sor[n]
                if tol < 0:
                    b += 1
                elif tol > 0:
                    c -= 1
                else:
                    li.append([sor[n],sor[b],sor[c]])
                    b += 1
                    while sor[b] == sor[b - 1] and b < c:
                        b += 1

        return li
                    

