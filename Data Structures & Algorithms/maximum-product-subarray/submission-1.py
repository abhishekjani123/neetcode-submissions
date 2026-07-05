class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1

        for n in nums:
            tmp = n * curmax
            curmax = max(n, n * curmax, n * curmin)
            curmin = min(n, tmp, n * curmin)
            res = max(res, curmax)
        return res