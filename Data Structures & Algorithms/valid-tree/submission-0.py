class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        # Define Adjacency list for nodes and their links
        premap = { i: [] for i in range(n)}

        # update the nodes and pre in the premap
        for u, v in edges:
            premap[u].append(v)
            premap[v].append(u)
        
        # create a visit set
        visit = set()
        #check the two condition in dfs
        def dfs(u, v):
            if u in visit:
                return False
            visit.add(u)
            for nei in premap[u]:
                if nei == v:
                    continue
                if not dfs(nei, u):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n


