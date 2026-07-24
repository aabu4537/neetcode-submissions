class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i : [] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        def dfs(crs):
            if graph[crs] == []:
                return True
            if crs in visit:
                return False
            visit.add(crs)
            for pre in graph[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            graph[crs] = []
            return True

        for crs in graph:
            if not dfs(crs): return False
        

        return True
        