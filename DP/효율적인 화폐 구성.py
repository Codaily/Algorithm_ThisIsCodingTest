import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nlist = []
for _ in range(n):
    nlist.append(int(input()))

dp = [10001] * (m+1)
dp[0] = 0
for i in range(n):
    for j in range(nlist[i], m+1):
        dp[j] = min(dp[j], dp[j-nlist[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
