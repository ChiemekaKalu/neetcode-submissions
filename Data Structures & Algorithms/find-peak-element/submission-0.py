class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1

        while low != high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]: #upward slope, search in that direction
                low = mid + 1
            else: #downward slope because nums[mid] > nums[mid + 1]
                high = mid 
        return low
        

                
        