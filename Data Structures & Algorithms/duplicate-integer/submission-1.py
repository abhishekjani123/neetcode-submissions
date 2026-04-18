class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u = set(nums)
        a = len(nums)
        b = len(u)
        if a == b:
            return False
        else:
            return True
        