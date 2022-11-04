class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodes = {i : set() for i in range(n)}
        ancestors = {}
        for edge in edges:
            nodes[edge[1]].add(edge[0])
        
        def findAncestors(node):
            if node in ancestors:
                return list(ancestors[node])
            
            a = set()
            for e in nodes[node]:
                a.add(e)
                a.update(findAncestors(e))
            
            ancestors[node] = a
            return a
        
        
        sol = []
        for i in range(n):
            if i not in ancestors:
                findAncestors(i)
            sol.append(sorted(list(ancestors[i])))
        return sol
        
        
            
        