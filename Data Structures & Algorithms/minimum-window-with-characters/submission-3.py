from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        tCount = Counter(t)
        need = len(tCount)
        windowC = {}
        have = 0
        res = [-1, -1] 
        resLen = float('inf')
        l = 0

        for r, right in enumerate(s):
            windowC[right] = 1 + windowC.get(right, 0)
            if right in tCount and windowC[right] == tCount[right]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                windowC[s[l]] -= 1
                if s[l] in tCount and windowC[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""