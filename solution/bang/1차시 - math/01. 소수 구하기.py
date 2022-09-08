M, N = map(int, input().split())

# 에라토스테네스의 체 활용

# 소수인지 판별하기 위한 배열 생성
prime_arr = [True]*(N+1)
prime_arr[0] = False
prime_arr[1] = False

# 반복문을 통해서 소수를 모두 찾아냄
for i in range(2, N+1):
    if prime_arr[i] == True: #특정 값이 아직까지 소수인 경우
        j = 2
        while(i*j) <= N:
            prime_arr[i*j] = False # i의 배수 값을 소수가 아니라고 판별
            j += 1

# M부터 N까지의 소수를 출력
for i in range(M, N+1):
    if prime_arr[i]:
        print(i)