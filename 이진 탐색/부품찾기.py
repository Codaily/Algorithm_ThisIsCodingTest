import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

for ml in mlist:
    start = 0
    end = n-1
    yesOrNo = "no"
    while start <= end:
        mid = (start+end)//2

        if ml > nlist[mid]:
            start = mid + 1
        elif ml < nlist[mid]:
            end = mid - 1
        else:
            yesOrNo = "yes"
            break
    print(yesOrNo, end = " ")
    