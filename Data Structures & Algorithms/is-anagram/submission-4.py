from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC = Counter(s)
        sT = Counter(t)

        return sC == sT
        


        