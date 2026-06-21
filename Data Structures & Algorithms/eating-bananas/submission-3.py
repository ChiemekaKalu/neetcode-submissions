import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles, hours, k):
            timeSpent = 0
            for p in piles:
                timeSpent += math.ceil(p/k)
                if timeSpent > hours:
                    return False
            return True
        
        low = 1
        high = max(piles)
        
        while low != high:
            mid = (low + high) // 2 
            if canEatAll(piles, h, mid):
                high = mid
            else:
                low = mid + 1
        
        return low # we could also return high here because 


        


