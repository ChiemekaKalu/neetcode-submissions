from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Checker = Counter(s1)
        windowSize = len(s1)
        for left in range(0, len(s2) - windowSize + 1):
            right = left + windowSize
            s2Checker = Counter(s2[left:right])
            if s1Checker == s2Checker:
                return True
        return False
