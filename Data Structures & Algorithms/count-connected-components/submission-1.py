class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for l, r in edges:
            graph[l].append(r)
            graph[r].append(l)
        visited = set()
        prev = -1
        res = 0
        def dfs(cur, prev, cycle, i):
            if cur in cycle:
                return
            edges = graph[cur]
            for edge in edges:
                if edge in cycle:
                    continue
                cycle.append(cur)
                dfs(edge, cur, cycle, i + 1)
            visited.add(cur)
            return
        for i in range(n):
            if i not in visited:
                visited.add(i)
                res += 1
                dfs(i, -1, [], 0)
        return res