import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [1, 0, -1, 0 ] 
dy = [0, 1, 0, -1] 

def dfs(cnt):
    global zeroCnt

    # 벽 3개 생성 완료
    if cnt == 3:
        _graph = graph[:]

        virus = 0
        for y in range(n):
            for x in range(m):
                if _graph[y][x] == 2:
                    for i in range(4):
                        ny = y+dy[i]
                        nx = x+dx[i]
                        if ny >= 0 and nx >= 0 and ny < n and nx < m:
                           if _graph[ny][nx] == 0:
                                _graph[y][x] = 2
                                virus += 1
        return

    # 벽 만듦
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                graph[i][j] = 0
                cnt -= 1

