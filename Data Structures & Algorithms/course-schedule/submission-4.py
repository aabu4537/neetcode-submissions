class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {i:[] for i in range(numCourses)}
        visit = set()
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        def dfs(crs):
            if courses[crs] == []: return True
            if crs in visit: return False

            visit.add(crs)
            for pre in courses[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            courses[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs): return False

        return True
        