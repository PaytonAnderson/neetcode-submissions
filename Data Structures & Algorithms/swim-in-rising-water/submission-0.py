class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        visited.add((0, 0))
        n = len(grid)
        minheap = [[grid[0][0], 0, 0]]
        while minheap:
            level, i, j = heapq.heappop(minheap)
            if i == n - 1 and j == n - 2 or i == n - 2 and j == n - 1:
                return max(level, grid[n-1][n-1])
            if i != 0:
                if (i - 1, j) not in visited:
                    heapq.heappush(minheap, [max(level, grid[i - 1][j]), i - 1, j])
                    visited.add((i - 1, j))
            if j != 0:
                if (i, j - 1) not in visited:
                    heapq.heappush(minheap, [max(level, grid[i][j - 1]), i, j - 1])
                    visited.add((i, j - 1))
            if i < n - 1:
                if (i + 1, j) not in visited:
                    heapq.heappush(minheap, [max(level, grid[i + 1][j]), i + 1, j])
                    visited.add((i + 1, j))
            if j < n - 1:
                if (i, j + 1) not in visited:
                    heapq.heappush(minheap, [max(level, grid[i][j + 1]), i, j + 1])
                    visited.add((i, j + 1))
        return -1
