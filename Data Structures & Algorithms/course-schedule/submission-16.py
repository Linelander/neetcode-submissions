from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # "1 requires 2"

        indeg = [0] * numCourses
        adj = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[pre].append(crs)    # shows prereqs and the courses that have them
            indeg[crs] += 1         # how many prereqs this course has

        q = deque(i for i in range(numCourses) if indeg[i] == 0)

        # the actual topo sort
        finish = 0 # counting how many course we can finish
        while q:
            fq = q.popleft()
            finish += 1 # we've finished this course
            for crs in adj[fq]:
                indeg[crs] -= 1
                if indeg[crs] == 0: # we CAN finish this other course that depended on fq
                    q.append(crs)

        return finish == numCourses
