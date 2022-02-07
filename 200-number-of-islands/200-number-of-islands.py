class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(y, x):
            grid[y][x] = "-1"
            if y != 0 and grid[y - 1][x] == "1": #left
                dfs(y - 1, x)
            if y < len(grid)-1 and grid[y + 1][x]=="1":
                dfs(y + 1, x)
            if x != 0 and grid[y][x - 1]=="1":
                dfs(y, x - 1)
            if x < len(grid[0])-1 and grid[y][x + 1]=="1":
                dfs(y, x + 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count