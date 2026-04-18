class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = 0
        l = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    s = nums[i] + nums[j]
                    if s == target:
                        l.append(i)
                        l.append(j)
                        return l
                    else:
                        s = 0

        