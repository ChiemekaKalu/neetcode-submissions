class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        l = 0
        r = n - 1
        res = 0
        
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                res += leftMax - height[l]
                l += 1
                leftMax = max(height[l], leftMax)
            else: #rightMax < leftMax or rightMax == leftMax
                res += rightMax - height[r]
                r -= 1
                rightMax = max(height[r], rightMax)
        
        return res

        