from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        longest = 0
        windowC = Counter()
        for right, char in enumerate(s):
            windowC[char] += 1

            while len(windowC) > 2:
                first = s[left]
                windowC[first] -= 1
                left += 1
                if windowC[first] == 0:
                    del windowC[first]
            
            if len(windowC) == 2:
                longest = max(longest, right - left + 1)

        return longest if len(windowC) == 2 else len(s)


        