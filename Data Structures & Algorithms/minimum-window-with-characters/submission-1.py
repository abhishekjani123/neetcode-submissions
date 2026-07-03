class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        reslen = float('infinity')
        res = [-1, -1]
        l = 0
        total_count = defaultdict(int)
        window_count = defaultdict(int)
        for i in range(len(t)):
            total_count[t[i]] += 1
        have = 0
        need = len(total_count)

        for r in range(len(s)):
            window_count[s[r]] += 1

            if s[r] in total_count and total_count[s[r]] == window_count[s[r]]:
                have += 1
            
            while have == need:
                window_count[s[l]] -= 1
                window_size = r - l + 1
                if window_size < reslen:
                    reslen = window_size
                    res = [l,r]
                if s[l] in total_count and window_count[s[l]] < total_count[s[l]]:
                    have -= 1
                l +=1
            
        if reslen != float('infinity'):
            return s[res[0]:res[1]+1]
        else:
            return ""

