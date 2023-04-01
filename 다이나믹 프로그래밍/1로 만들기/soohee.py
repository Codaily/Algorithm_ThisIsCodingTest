arr =  [0] * 100

def makeOne(x):
    
    for i in range(2,x+1):
        arr[i] = arr[i-1] + 1
        if i % 5 == 0 and arr[i] > arr[ i // 5 ] + 1:
            arr[i] = arr[ i // 5 ] + 1
        if i % 3 == 0 and arr[i] > arr[ i // 3 ] + 1:
            arr[i] = arr[ i // 3 ] + 1
        if i % 2 == 0 and arr[i] > arr[ i // 2 ] + 1:
            arr[i] = arr[ i // 2 ] + 1
 
    return arr[x]

print(makeOne(26))