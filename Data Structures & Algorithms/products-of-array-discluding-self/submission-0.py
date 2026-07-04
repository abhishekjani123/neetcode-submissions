class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        a = [1] * n

        prefix = 1
        for i in range(n):
            a[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1,-1,-1):
            a[i] *= postfix
            postfix *= nums[i]
        
        return a