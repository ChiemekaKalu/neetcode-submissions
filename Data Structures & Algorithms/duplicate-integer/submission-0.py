class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set(nums)
        return len(nums) != len(dedup)
        