food = []
n = int(input())
food = list(map(int,input().split()))

for i in range(2, n):
    food[i] = max(food[i-1], food[i] + food[i-2] )
    
print(food[-1])