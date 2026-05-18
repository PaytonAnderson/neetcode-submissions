class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #graph of visited node and current min time
        visited = {k:0}
        graph = {i:[] for i in range(1, n + 1)}
        for u, v, t in times:
            graph[u].append([v, t])
        #track current time and highest time required to reach a node
        q = deque([k])
        while q:
            cur = q.popleft()
            time = visited[cur]
            adj = graph[cur]
            for v, t in adj:
                if v in visited:
                    if t + time < visited[v]:
                        visited[v] = t + time
                        q.append(v)
                else:
                    visited[v] = time + t
                    q.append(v)

        high = 0
        for key, value in visited.items():
            high = max(high, value)
        if len(visited) < n:
            return -1
        return high
