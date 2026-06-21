class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        n = len(nums)
        for i in range(0, n+1):
            if i not in numSet:
                return i
                
        