class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        lenx , leny = len(grid), len(grid[0])
        
        def dfs(r,c):
            if r <0 or r>=lenx or c<0 or c>=leny or grid[r][c] != "1":
                return 
            grid[r][c] = "0"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)  
            
        
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans+=1
        
        return ans
                    
        