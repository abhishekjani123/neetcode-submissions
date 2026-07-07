class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #edge case
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        rep = set()
        rep.add(0)

        for i in range(len(nums) - 1, -1, -1):
            srep = set()
            for num in rep:
                srep.add(num + nums[i])
                srep.add(num)
            rep = srep
        
        if target in rep:
            return True 
        else:
            return False