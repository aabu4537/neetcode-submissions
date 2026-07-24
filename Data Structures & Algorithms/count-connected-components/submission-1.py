class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i: [] for i in range(n)}
        visit = set()
        count = 0
        for node, nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)

        def dfs(node):
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit: dfs(nei)
            return    
        
        for node in graph:
            if node not in visit:
                dfs(node)
                count +=1
        
        return count

        