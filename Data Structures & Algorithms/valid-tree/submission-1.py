class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for l, r in edges:
            graph[l].append(r)
            graph[r].append(l)
        visited = set()
        prev = -1
        def dfs(cur, prev, cycle):
            if cur in cycle:
                print(cur, prev, cycle)
                return False
            edges = graph[cur]
            for edge in edges:
                if edge == prev:
                    continue
                cycle.append(cur)
                if not dfs(edge, cur, cycle):
                    return False
                cycle.pop()
            visited.add(cur)
            return True

        if not dfs(0, -1, []):
            return False
        if len(visited) != n:
            return False
        return True
