from collections import deque
n, m, k, x = map(int, input().split()) # n은 도시의 개수, m은 도로의 개수, k는 거리 정보, x는 출발 도시의 번호

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())  
    graph[a] += [b]

now = x
queue = deque()
queue.append(now)
visited = [0 for _ in range(n+1)]

while queue:
    now = queue.popleft()
    for i in graph[now]:
        if visited[i] == 0 : 
            queue.append(i)
            visited[i] += visited[now] + 1

answer = []
for i , j in enumerate(visited):
    if j == k:
        answer.append(i) 

if answer :
    for i in answer:
        print(i)
else:
    print(-1)







