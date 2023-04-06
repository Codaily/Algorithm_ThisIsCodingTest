import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nlist = list(map(int, input().split()))

def count(num):
    cnt = 0
    for nl in nlist:
        if nl > num:
            cnt += nl - num
    return cnt

start = 0
end = max(nlist)
answer = 0
while start <= end:
    mid = (start + end) // 2

    num = count(mid)

    if num > m :
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

