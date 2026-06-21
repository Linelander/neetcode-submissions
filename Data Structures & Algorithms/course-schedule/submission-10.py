class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        
        if not prerequisites: return True
        seen = []

        seen = set()    # fully cleared, safe
        path = set()    # open on the current stack

        def dfs(course):
            if course in path:
                return False
            if course in seen:
                return True
            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            path.remove(course)
            seen.add(course)
            return True


        return all(dfs(c) for c in range(numCourses))