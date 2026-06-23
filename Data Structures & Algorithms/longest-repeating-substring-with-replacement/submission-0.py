from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_len = 0
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            # update frequency of s[r]
            count[s[r]] += 1
            # track the highest frequency in current window
            max_freq = max(max_freq, count[s[r]])
            
            # window invalid: need to replace more than k characters
            if (r - l + 1) - max_freq > k:
                # shrink from left
                count[s[l]] -= 1
                l += 1
                # optional: recalc max_freq when shrinking? 
                # (it's safe to keep it because we only increase max_len)
            
            max_len = max(max_len, r - l + 1)
        
        return max_len