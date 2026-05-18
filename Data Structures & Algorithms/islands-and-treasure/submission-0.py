class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #bfs from treasures
        #q for path, if next path value > value +1 add
        #find treasures
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append([i, j, 0])
        while q:
            i, j, val = q.popleft()
            #extend outwards
            if i != 0 and grid[i - 1][j] > (val + 1):
                grid[i - 1][j] = val + 1
                q.append([i - 1, j, val + 1])
            if i != len(grid) - 1 and grid[i + 1][j] > (val + 1):
                grid[i + 1][j] = val + 1
                q.append([i + 1, j, val + 1])
            if j != 0 and grid[i][j - 1] > (val + 1):
                grid[i][j - 1] = val + 1
                q.append([i, j - 1, val + 1])
            if j != len(grid[i]) - 1 and grid[i][j + 1] > (val + 1):
                grid[i][j + 1] = val + 1
                q.append([i, j + 1, val + 1])

