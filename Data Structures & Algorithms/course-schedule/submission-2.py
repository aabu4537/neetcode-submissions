class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {i : [] for i in range(numCourses)}
        visit = set()
        for co, pre in prerequisites:
            courses[co].append(pre)

        def dfs(co):
            if courses[co] == []:
                return True
            if co in visit:
                return False
            
            visit.add(co)
            for pre in courses[co]:
                if not dfs(pre): return False
            visit.remove(co)
            courses[co] = []
            return True

        for co in courses:
            if not dfs(co): return False

        return True
    
        