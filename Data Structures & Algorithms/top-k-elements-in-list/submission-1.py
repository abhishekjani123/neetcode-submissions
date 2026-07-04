from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter= Counter(nums)

        # Secons Step: Empty List

        a = [[] for _ in range(len(nums)+1)]

        for num, counts in counter.items():
            a[counts].append(num)
        
        result = []
        for i in range(len(a) - 1, 0 , -1):
            for n in a[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
        
