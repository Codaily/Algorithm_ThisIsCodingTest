import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
dp = [0] * n
dp[0] = nlist[0]
dp[1] = max(nlist[0], nlist[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+nlist[i])
print(dp[-1])
