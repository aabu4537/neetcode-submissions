class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(numCourses)}
        res = []
        visit = set()
        cycle = set()

        for crs, pre in prerequisites:
            graph[crs].append(pre)


        def helper(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in graph[crs]:
                if not helper(pre): return False
            cycle.remove(crs)
            visit.add(crs)

            res.append(crs)
            return True


        for crs in graph:
            if not helper(crs):
                return []

        return res
