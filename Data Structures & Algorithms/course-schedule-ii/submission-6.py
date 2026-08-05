class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        res = []

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] +=1
        q = deque()


        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        while q:
            node = q.popleft()
            res.append(node)
            for crs in graph[node]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)

        if len(res) == numCourses:
            return res
        else:
            return []


        return res
        
