class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        t1 = defaultdict(int)

        if len(s) == len(t):
            for i in range(len(s)):
                s1[s[i]] += 1
                t1[t[i]] += 1
            return True if s1 == t1 else False
        else:
            return False