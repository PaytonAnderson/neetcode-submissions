class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for prev, dest in tickets:
            if prev in graph:
                graph[prev].append(dest)
            else:
                graph[prev] = [dest]
        def dfs(path):
            if len(path) == len(tickets) + 1:
                return path
            cur = path[-1]
            if cur not in graph:

                return []
            adj = graph[cur]
            adj = sorted(adj)
            i = 0
            for node in adj:
                graph[cur].remove(node)
                path.append(node)
                temp = dfs(path)
                if temp:    
                    return temp
                path.pop()
                graph[cur].append(node)
                i += 1
            return []
        res = dfs(["JFK"])
        return res

