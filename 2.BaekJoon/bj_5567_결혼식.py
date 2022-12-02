N = int(input())
M = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [[0]*(N+1) for _ in range(N+1)]

friend = [0 for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    graph[A][B] = 1
    graph[B][A] = 1
    
def dfs(r,c,cnt):
    if cnt > 1:
        return
    friend[c] = 1
    for new_c in range(N+1):
        if graph[c][new_c]:
            dfs(c,new_c,cnt+1)
            
for col in range(2,N+1):
    if graph[1][col]:
        dfs(1,col,0)
        
friend[1] = 0
print(friend.count(1))
