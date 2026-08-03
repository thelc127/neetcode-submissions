class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        lp, rp = 0, len(heights) - 1

        while lp <rp:
            width = rp - lp
            height = min(heights[rp], heights[lp])
            area = height * width
            maxarea = max(area, maxarea)

            if heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp+=1


        return maxarea



        

        