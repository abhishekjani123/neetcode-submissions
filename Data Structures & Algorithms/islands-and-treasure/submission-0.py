class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0
        
        ROW = len(grid)
        COL = len(grid[0])
        q = deque()
        chest_distance = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    

        distance = [(1,0), (-1,0), (0,-1), (0,1)]

        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in distance:
                    row = r + dr
                    col = c + dc
                    if row >= 0 and col >= 0 and row < ROW and col < COL and grid[row][col] == 2147483647:
                        grid[row][col] = grid[r][c] + 1
                        q.append((row,col))
        return None

