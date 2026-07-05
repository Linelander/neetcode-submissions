class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)


        cycle = set()
        done = set()
        result = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in done:
                return True

            cycle.add(crs)

            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            done.add(crs)
            result.append(crs)
            cycle.remove(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return result