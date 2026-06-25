class Solution:

    def findMin(self, nums):
            low = 0
            high = len(nums) - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]: #our mid element is greater than our highest, so search that side
                        low = mid + 1
                else:
                    high = mid 
            return low 

    def search(self, nums: List[int], target: int) -> int:
        #first thing to do is find our min, which will be our "pivot"
        #the pivot tells us which side of the array we should be looking in
        #both sides will be sorted in some type of way 

        pivot = self.findMin(nums)
        
        if nums[pivot] <= target <= nums[-1]:
            low = pivot
            high = len(nums) -1 
        else:
            low = 0
            high = pivot - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1 


                
    
        

