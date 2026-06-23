class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        
        l = 0
        r = 0
        
        seen = set()
        maxL = 0
        for char in s:
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            r += 1
            maxL = max(maxL, r - l)
        return maxL