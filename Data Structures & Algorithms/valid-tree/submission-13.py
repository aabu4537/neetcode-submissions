class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i : [] for i in range(n)}
        visit = set()

        for e, r in edges:
            graph[e].append(r)
            graph[r].append(e)
        
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for edge in graph[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node): return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        