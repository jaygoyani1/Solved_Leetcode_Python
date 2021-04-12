class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        x = len(grid)
        y = len(grid[0])
        
        def dfs(i,j):
            if i<0 or i>=x or j<0 or j>=y or grid[i][j] == "0":
                return 0
            grid[i][j] = "0"
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return 1
        total = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == "1":
                    total += dfs(i,j)
        return total