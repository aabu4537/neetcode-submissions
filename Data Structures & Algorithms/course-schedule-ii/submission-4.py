class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        res = []
        seen = set()
        visited = set()

        for crs, pre in prerequisites:
            graph[crs].append(pre)
        print(graph)
        
        def helper(crs):
            if crs in seen:
                return False
            if crs in visited:
                return True

            seen.add(crs)
            for pre in graph[crs]:
                if not helper(pre): return False
            seen.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in graph:
            if not helper(crs):
                return []

        return res
        
