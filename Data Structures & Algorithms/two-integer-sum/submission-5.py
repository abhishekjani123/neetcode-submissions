class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in p:
                return [p[diff], i]
            p[n] = i