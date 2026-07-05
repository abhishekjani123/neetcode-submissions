class Solution:
    def rob(self, nums: List[int]) -> int:

        a = self.help(nums[1:])
        b = self.help(nums[:-1])
        return max(nums[0], a, b)

    def help(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2