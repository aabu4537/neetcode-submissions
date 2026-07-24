class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        tree = {i: [] for i in range(n)}
        visit = set()

        for one, two in edges:
            tree[one].append(two)
            tree[two].append(one)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for i in tree[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n