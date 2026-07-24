class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        nodes = {i: [] for i in range(n)}
        visit = set()
        count = 0

        for node, nei in edges:
            nodes[node].append(nei)
            nodes[nei].append(node)

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in nodes[node]:
                dfs(nei)
            return
                

        for node in nodes:
            if node not in visit:
                dfs(node)
                count +=1
        
        return count