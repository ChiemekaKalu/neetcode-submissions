class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def checkArea(l, r):
            height = min(heights[l], heights[r])
            width = r - l
            return height * width
        maxWater = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            maxWater = max(maxWater, checkArea(l,r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater

        

        
        