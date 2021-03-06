# 다이나믹프로그래밍 (Dynamic Programing)
##### 메모리 공간을 약간 더 사용해 연산 속도를 비약적으로 증가시키는 방법
##### 다이나믹프로그래밍은 큰 문제를 작게 나누고, 같은 문제라면 한번만 풀어 문제를 효율적으로 해결하는 알고리즘 방법이다.

다이나믹 프로그래밍의 대표적인 문제가 피보나치 수열이다.

```python
# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
```


![image](https://user-images.githubusercontent.com/55631147/133082063-fd3fa6d5-a1aa-4089-8c64-628045eb887a.png)

이렇게 피보나치 수열을 짜게 되면, O(2ᴺ)의 시간복잡도를 가지게 된다.
빅오 표기법 기준으로 f(30)을 계산하려면 10억의 연산을 해야한다.
따라서, 효율적인 해법이 필요한데 그것이 다이나믹 프로그래밍이다.

## 다이나믹 프로그래밍 사용하자.
* 다이나믹 프로그래밍의 사용조건을 만족하는지 확인한다.
    1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있다 
    2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결한다 


## 메모제이션 (Memoization) 
![image](https://user-images.githubusercontent.com/55631147/133082195-13d1f278-d319-400f-9c94-cab2734d54b6.png)

큰 문제를 해결 하기 위해 작은 문제를 호출한다고 하여 Top-down 방식이라고 한다.
* 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나이다 
* 한 번 계산한 결과를 메모리 공간에 메모하는 기법이다 
    * 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져온다
    * 값을 기록해 놓는다는 점에서 캐싱(Caching) 이라고도 한다


### Top-down vs Bottom-up
* 탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고도 한다
* 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다
    * 결과 저장용 리스트는 DP 테이블이라고 부른다



### 피보나치 수열 : 탑다운 DP ( 메모제이션 코드 )
메모제이션을 사용할 경우 시간 복잡도는 O(N) 
```python
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))
```

### 피보나치 수열 : 보텀업 DP 
```python
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

## 다이나믹 프로그래밍 vs 분할 정복

* 다이나믹 프로그래밍과 분할 정복은 모두 **최적 부분 구조** 를 가질 때 사용할 수 있다

  * 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황 

* 다이나믹 프로그래밍과 분할 정복의 차이점은 **부분 문제의 중복** 이다

    * 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다 

    * 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다 

