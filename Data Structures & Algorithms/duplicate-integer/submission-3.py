class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)

        return False if len(n) == len(nums) else True