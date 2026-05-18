class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1, len(edges) + 1)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def dfs(cur, prev, cycle):
            edges = graph[cur]
            for edge in edges:
                if edge == prev:
                    continue
                if edge in cycle:
                    cycle = cycle[cycle.index(edge):]
                    cycle.append(edge)
                    return cycle
                cycle.append(edge)
                res = dfs(edge, cur, cycle)
                if res != []:
                    return res
                cycle.pop()
            return []
        cycle = dfs(1, -1, [])
        possible = []
        for i in range(len(cycle) - 1):
            x, y = cycle[i], cycle[i + 1]
            l = min(x, y)
            r = max(x, y)
            possible.append([l, r])
        i = 0
        while len(possible) > 1:
            if edges[i] in possible:
                possible.remove(edges[i])
            i += 1
        return possible[0]