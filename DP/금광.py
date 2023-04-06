import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dy = [-1,0,1]

for _ in range(t):
    n, m = map(int, input().split())
    nlist = list(map(int, input().split()))
    max_num = 0
    dp = [[0]*(m+1) for _ in range(n+2)]
    for j in range(1,m+1):
        for i in range(1, n+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + nlist[m*(i-1)+(j-1)]
            if max_num < dp[i][j]:
                max_num = dp[i][j]
    print(max_num)

