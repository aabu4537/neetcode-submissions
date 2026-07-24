class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i:[] for i in range(n)}
        counter = 0
        visit = set()
        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)
        
        print(graph)
        def dfs(e):
            if e in visit:
                return
            visit.add(e)
            for nei in graph[e]:
                dfs(nei)
            

        for e in graph:
            if e not in visit:
                dfs(e)
                counter+=1

        return counter
        