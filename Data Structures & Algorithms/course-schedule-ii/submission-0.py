class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        #adjacency list
        
        # states:
        # visited (in output)
        # visiting (in cycle, not output)
        # unvisited: neither
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit: #?
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # now that we've visited all prereqs,
            # we're done processing this course
            visit.add(crs)
            cycle.remove(crs) # new path
            output.append(crs)
            return True # everything worked

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output