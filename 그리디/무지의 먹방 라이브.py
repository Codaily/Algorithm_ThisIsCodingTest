def solution(food_times, k):
    idx=0
    second=0
    
    while second <= k:
        idx = idx % len(food_times)
        if len(food_times)==food_times.count(0):
            return -1
        if food_times[idx] > 0:
            food_times[idx] -=1
            second+=1
        idx+=1
        
    return idx

# 효율성 관련 풀어야함.
# import heapq
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1

#     heap = []
#     for i in range(len(food_times)):
#         heapq.heappush(heap, (food_times[i], i+1))


#   return idx

print(solution([3,1,2], 5))