class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        windowC = Counter()
        for right, char in enumerate(s):
            windowC[char] += 1

            while len(windowC) > k:
                first = s[left]
                windowC[first] -= 1
                left += 1
                if windowC[first] == 0:
                    del windowC[first]
            
            if len(windowC) == k:
                longest = max(longest, right - left + 1)

        return longest if len(windowC) == k else len(s)
