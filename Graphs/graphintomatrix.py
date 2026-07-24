m=6
n=5
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
# lst=[[] for _ in range(n+1)]
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
for u,v in edges:
    matrix[u].append(v)
    matrix[v].append(u)
print(matrix)