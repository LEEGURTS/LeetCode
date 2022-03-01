class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def check(x,y):
            if x < 0 or x >= len(grid):
                return False
            elif y < 0 or y >= len(grid[0]):
                return False
            return True
        def dfs(x,y):
            stack = []
            stack.append((x,y))
            while stack:
                v = stack.pop()
                if grid[v[0]][v[1]] is '1':
                    grid[v[0]][v[1]] = 0
                    if check(v[0]+1,v[1]):
                        stack.append((v[0]+1,v[1]))
                    if check(v[0],v[1]+1):
                        stack.append((v[0],v[1]+1))
                    if check(v[0]-1,v[1]):
                        stack.append((v[0]-1,v[1]))
                    if check(v[0],v[1]-1):
                        stack.append((v[0],v[1]-1))
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result