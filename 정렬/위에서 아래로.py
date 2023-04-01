import sys
input = sys.stdin.readline
n = int(input())
nlist = []

for _ in range(n):
    nlist.append(int(input()))

nlist.sort(reverse=True)

print(*nlist)