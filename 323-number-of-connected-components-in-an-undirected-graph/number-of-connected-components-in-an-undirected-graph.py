class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Using UNION FIND ( UNION DISJOIN SETS)   
        parent = [i for i in range(n)]
        rank = [1]*n #number of nodes
        
        #FIND
        def find(n1): #find root parent
            res = n1
            while res!= parent[res]: #recursively find parent 
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        #UNION
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        #Go through edges
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res