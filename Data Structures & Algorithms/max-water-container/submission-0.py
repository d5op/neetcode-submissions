class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lar = 0
        for n in range(len(heights)):
            for z in range(n+1, len(heights)):
                curwidth = z - n
                curheight = min(heights[z], heights[n])
                cursize =curheight * curwidth
                if cursize > lar:
                    lar = cursize
        return lar