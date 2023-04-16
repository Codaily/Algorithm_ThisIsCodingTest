import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().strip())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def bfs(b, a):
    queue = deque([[b, a]])
    nlist[b][a] = 0
    cnt = 1

    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if nlist[ny][nx] == 1:
                    queue.append([ny, nx])
                    nlist[ny][nx] = 0
                    cnt += 1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if nlist[i][j] == 1:
            result.append(bfs(i, j))

result = sorted(result)
print(len(result))
for i in range(len(result)):
    print(result[i])