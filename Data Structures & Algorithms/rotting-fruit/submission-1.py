class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        time = 0
        fresh_orange = 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_orange += 1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh_orange > 0:
            qlen = len(q)
            for i in range(qlen):
                r1, c1 = q.popleft()
                
                for dr, dc in directions:
                    rows = dr + r1
                    cols = dc + c1

                    if rows >= 0 and cols >= 0 and rows < row and cols < col and grid[rows][cols] == 1:
                        grid[rows][cols] = 2
                        fresh_orange -= 1
                        q.append((rows, cols))
            time += 1
        
        if fresh_orange == 0:
            return time
        else:
            return -1
