class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        print(num)
        return False if len(num) == len(nums) else True