class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or at a water cell ('0'), stop
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited by setting it to '0'
            grid[r][c] = '0'
            
            # Recursively visit all adjacent neighbors (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                # If we find land ('1'), it's the start of a new island
                if grid[r][c] == '1':
                    island_count += 1
                    # Use DFS to sink the entire island
                    dfs(r, c)
                    
        return island_count