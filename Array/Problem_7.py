class Solution:
    def numberOfSubmatrices(self, grid):
        n, m = len(grid), len(grid[0])

        gx = [[0] * m for _ in range(n)]  # (0,0) to (i,j), how many Xs
        gy = [[0] * m for _ in range(n)]  # (0,0) to (i,j), how many Ys

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    gx[0][0] = 1 if grid[0][0] == 'X' else 0
                    gy[0][0] = 1 if grid[0][0] == 'Y' else 0
                else:
                    
                    if i == 0:
                        gx[0][j] = gx[0][j - 1]
                        gy[0][j] = gy[0][j - 1]
                    elif j == 0:
                        gx[i][0] = gx[i - 1][0]
                        gy[i][0] = gy[i - 1][0]
                    else:
                        gx[i][j] = gx[i - 1][j] + gx[i][j - 1] - gx[i - 1][j - 1]
                        gy[i][j] = gy[i - 1][j] + gy[i][j - 1] - gy[i - 1][j - 1]
                    if grid[i][j] == 'X':
                        gx[i][j] += 1
                    if grid[i][j] == 'Y':
                        gy[i][j] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if gx[i][j] == gy[i][j] and gx[i][j] > 0:
                    res += 1

        return res
