class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookSet = set(nums)
        longest = 0

        for num in lookSet:
            if num - 1 in lookSet:
                continue
            else:
                length = 1
                while num + length in lookSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
