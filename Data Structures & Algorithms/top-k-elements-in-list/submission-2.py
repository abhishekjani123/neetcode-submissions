from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        a = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            a[c].append(num)
        
        res = []

        for i in range(len(a)-1,0,-1):
            for nos in a[i]:
                res.append(nos)
                if len(res) == k:
                    return res
