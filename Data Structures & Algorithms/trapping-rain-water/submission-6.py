from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            # The smaller side determines the trapped water bound
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                # Water above current bar is bounded by left_max here
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                # Water above current bar is bounded by right_max here
                water += right_max - height[right]

        return water
