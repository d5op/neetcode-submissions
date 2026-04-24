class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        lar = 0
        for n in range(len(heights)):
            for z in range(n+1, len(heights)):
                curwidth = z - n
                curheight = min(heights[z], heights[n])
                cursize =curheight * curwidth
                if cursize > lar:
                    lar = cursize
        return lar
        '''
        l, r = 0, len(heights) - 1
        maxsize = 0
        while l < r:
            curwidth = r-l
            curheight = min(heights[r], heights[l])
            cursize = curheight * curwidth
            if cursize > maxsize:
                maxsize = cursize
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxsize