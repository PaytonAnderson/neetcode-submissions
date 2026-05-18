class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        oceans = [[[False, False] for x in y ] for y in heights]
        res = []
        # oceans [Pacific(0), Atlantic(1)]
        for j in range(len(heights[0])):
            dfs(0, j, heights, oceans, 0, 0)
            dfs(len(heights) - 1, j, heights, oceans, 1, 0)
        for i in range(len(heights)):
            dfs(i, 0, heights, oceans, 0, 0)
            dfs(i, len(heights[0]) - 1, heights, oceans, 1, 0)
        for i in range(len(oceans)):
            for j in range(len(oceans[0])):
                if oceans[i][j] == [True, True]:
                    res.append([i, j])
        return res

def dfs(i, j, heights, oceans, ocean, prev):
    if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[i]) or oceans[i][j][ocean] or prev > heights[i][j]:
        return
    oceans[i][j][ocean] = True
    dfs(i - 1, j, heights, oceans, ocean, heights[i][j])
    dfs(i + 1, j, heights, oceans, ocean, heights[i][j])
    dfs(i, j + 1, heights, oceans, ocean, heights[i][j])
    dfs(i, j - 1, heights, oceans, ocean, heights[i][j])
    return