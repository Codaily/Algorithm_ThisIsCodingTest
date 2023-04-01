from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1, 0, -1, 0 ] # 오른쪽 아래 왼쪽 위
dy = [0, 1, 0, -1] 

queue = deque([[0, 0, 1]])
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
def bfs(y, x, cnt):
    
    while queue:
        y, x, cnt = queue.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny >= 0 and nx >= 0 and ny < n and nx < m:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True 
                    queue.append([ny, nx, cnt+1])
    return cnt

print(bfs(0, 0, 0))



# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111