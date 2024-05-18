class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        root = range(n+1)
        aux1, aux2, aux3 = 0, 0, 0
        
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            i, j = find(i), find(j)
            if i == j: 
                return False
            root[i] = j
            return True

        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    aux2 += 1
                    aux3 += 1
                else:
                    aux1 += 1
        
        rootAux = root[:]
        
        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    aux2 += 1
                else:
                    aux1 += 1

        root = rootAux
        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    aux3 += 1
                else:
                    aux1 += 1

        return aux1 if aux2 == aux3 == n-1 else -1