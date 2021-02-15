class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        lenx, leny = len(image), len(image[0])
        
        def dfs(r,c):
            if r<0 or r>=lenx or c < 0 or c>= leny or image[r][c] != color:
                return
            
            image[r][c] = newColor
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image
        