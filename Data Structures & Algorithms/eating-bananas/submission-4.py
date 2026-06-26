import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles, h, k):
            spent = 0
            for p in piles:
                spent += math.ceil(p / k)
                if spent > h:
                    return False
            return True
        
        low = 1
        high = max(piles)

        while low != high:
            mid = (low + high) // 2
            if not canEatAll(piles, h, mid):
                low = mid + 1
            else:
                high = mid
        
        return low






