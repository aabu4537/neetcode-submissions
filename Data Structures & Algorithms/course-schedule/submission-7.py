class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i:[] for i in range(numCourses)}
        seen = set()

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False

            seen.add(crs)
            for pre in graph[crs]:
                if not dfs(pre): return False
            seen.remove(crs)
            return True

        for crs in graph:
            if not dfs(crs): return False

        return True
