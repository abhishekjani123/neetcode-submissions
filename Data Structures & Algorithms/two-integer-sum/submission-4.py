class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_value = {}

        for i in range(len(nums)):
            diff = target - int(nums[i])
            if diff in prev_value:
                return [prev_value[diff], i]
            prev_value[nums[i]] = i