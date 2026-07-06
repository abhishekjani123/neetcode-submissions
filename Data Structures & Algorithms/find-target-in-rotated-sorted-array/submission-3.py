class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res_ind = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                res_ind = m
                break
            else:
                if nums[l] <= nums[m]:
                    if nums[l] <= target and target < nums[m] :
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] < target and target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        return res_ind