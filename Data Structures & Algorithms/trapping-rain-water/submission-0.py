class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        total = 0

        while l < r:
            if height[l] < height[r]:
                left_max = max(height[l], left_max)
                t = left_max - height[l]
                total += t
                l += 1
            else:
                right_max = max(height[r], right_max)
                t = right_max - height[r]
                total += t
                r -= 1
        return total