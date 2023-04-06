import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
first, second = map(int, input().split())
answer = 0
for nl in nlist:
    nl -= first
    answer += 1
    if nl > 0:
        if nl % second == 0:
            answer += nl // second
        else:
            answer += nl // second + 1

print(answer)