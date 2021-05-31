class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        maximal = 0
        
        for i in range(m):
            
            if matrix[i][0] == "1":
                maximal = 1
                break
        for i in range(n):
            if matrix[0][i] == "1":
                maximal = 1
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    matrix[i][j] = 1 + min(int(matrix[i-1][j-1]), min(int(matrix[i-1][j]), int(matrix[i][j-1])))
                    maximal = max(maximal, matrix[i][j])
        return maximal*maximal
                
        