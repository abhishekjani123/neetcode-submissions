class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        a1 = len(nums)
        print(a1)
        a2 = len(unique)
        print(a2)
        return bool(a1!=a2)
         