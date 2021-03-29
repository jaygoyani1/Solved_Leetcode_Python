class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image[0]) or image[i][j] != color:
                return
            image[i][j] = newColor
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        dfs(sr,sc)
        return image