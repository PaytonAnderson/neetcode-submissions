class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for course, req in prerequisites:
            graph[course].append(req)
        res = []
        for i in range(numCourses):
            def dfs(cur, cycle):
                for req in graph[cur]:
                    if req in res:
                        continue
                    if req in cycle:
                        return False
                    cycle.append(req)
                    if not dfs(req, cycle):
                        return False
                    cycle.pop()
                res.append(cur)
                return True
            if i not in res:
                if not dfs(i, [i]):
                    return []
        return res
