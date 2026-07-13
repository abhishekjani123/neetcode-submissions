class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = defaultdict(int)

        for i, num in enumerate(nums):
            dif = target - num
            if dif in prev:
                return [prev[dif], i]
            prev[num] = i
