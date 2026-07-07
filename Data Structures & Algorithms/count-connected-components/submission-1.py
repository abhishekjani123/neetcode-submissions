class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        premap = { i : [] for i in range(n)}
        visit = [False] * n

        for u,v in edges:
            premap[u].append(v)
            premap[v].append(u)
        
        def dfs(u):
            for nei in premap[u]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res