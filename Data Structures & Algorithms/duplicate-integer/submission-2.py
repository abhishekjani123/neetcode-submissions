class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        a = len(n)
        b = len(nums)
        if a == b:
            return False
        else:
            return True
        