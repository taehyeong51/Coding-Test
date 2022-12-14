'''
첫째 줄 : a,b
둘째 줄 : 전체 문자의 수 N, 치환 가능한 문자쌍 수 M
'''
from collections import deque
num_input = map(int,input().split())
a,b = num_input
N,M = num_input

graph = [[] for _ in range(10001)]
for _ in range(M):
    i,j = num_input
    graph[i].append(j)
    graph[j].append(i)

q = deque()
q.append((a,0))
is_possible = False
visited = [0 for _ in range(10001)]
while q:
    now,dist = q.popleft()
    if now == b:
        is_possible = True
        break
    for next in graph[now]:
        if not visited[next]:
            visited[next] = 1
            q.append((next,dist+1))
            
if is_possible:
    print(dist)
else:
    print(-1)