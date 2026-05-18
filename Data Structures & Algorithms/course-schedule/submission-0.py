class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        for course, req in prerequisites:
            if req not in courses:
                courses[req] = None
            if course not in courses or courses[course] == None:
                courses[course] = [req]
            else:
                courses[course].append(req)
        for course in courses:
            def dfs(cur, visited):
                if courses[cur] == None:
                    return True
                reqs = courses[cur]
                print(reqs)
                print(visited)
                for req in reqs:
                    if req in visited:
                        return False
                    visited.append(req)
                    if not dfs(req, visited):
                        return False
                    visited.pop()
                courses[cur] = None
                return True
            if not dfs(course, [course]):
                return False
        return True