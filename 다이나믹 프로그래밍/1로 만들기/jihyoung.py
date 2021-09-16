# DP : Bottom-up
import sys
input = sys.stdin.readline

x = int(input())

# 앞선 결과값을 저장하고 나중에 다시 사용하는 방식! 결과값을 저장할 배열
d = [0 for _ in range(x + 1)]

for i in range(2, x+1):
    d[i] = d[i-1] + 1 # 1로 만들어야 하니까 다음꺼는 전꺼에 무조건 +1 해야 됨
    
    # 값 자체가 인덱스가 됨
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)


print('답' , d[x])

