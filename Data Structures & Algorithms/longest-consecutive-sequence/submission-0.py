class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            l = 0
            if n-1 not in num_set:
                l += 1
                while n + l in num_set:
                    l += 1
            longest = max(longest, l)
        return longest