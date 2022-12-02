H,N = map(int,input().split())
L = abs(H-N)+1
graph = [[0]*abs(L) for _ in range(abs(L))]

for r in range(L):
    for c in range(L):
        if r > c:
            graph[r][c] = 0

for c in range(L):
    graph[0][c] = 1
    
for r in range(1,L):
    for c in range(r,L):
        graph[r][c] = graph[r-1][c] + graph[r][c-1]
            
print(graph[-1][-1])

        