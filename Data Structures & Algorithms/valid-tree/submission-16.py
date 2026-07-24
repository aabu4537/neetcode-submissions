class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i : [] for i in range(n)}
        visit = set()
        for p, e in edges:
            graph[p].append(e)
            graph[e].append(p)
        
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node): return False
            return True
            
        return dfs(0, -1) and len(visit) == n