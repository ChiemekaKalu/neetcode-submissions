class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        preMax = [0] * n
        sufMax = [0] * n    

        currentMax = 0
        for i, h in enumerate(height):
            currentMax = max(currentMax, h)
            preMax[i] = currentMax 

        currentMax = 0
        for i in range(n - 1, -1, -1):
            h = height[i]
            currentMax = max(currentMax, h)
            sufMax[i] = currentMax

        maxWater = 0
        for i, h in enumerate(height):
            area = min(preMax[i], sufMax[i]) - h
            maxWater += area

        return maxWater
            
        
        


        