# 입력 값
N = int(input())
input_list = list(map(int, input().split()))

# 에라토스테네스의 체 활용

# 소수인지 판별하기 위한 배열 생성(주어지는 수는 1000이하의 자연수임.)
prime_arr = [True]*(1001)
prime_arr[0] = False
prime_arr[1] = False

# 반복문을 통해서 소수를 모두 찾아냄
for i in range(2, 1001):
    if prime_arr[i] == True: #특정 값이 아직까지 소수인 경우
        j = 2
        while(i*j) <= 1000:
            prime_arr[i*j] = False # i의 배수 값을 소수가 아니라고 판별
            j += 1

# 소수의 개수 구하기
num = 0 # 소수의 개수 초기값
for i in range(0, N):
    val = input_list[i]
    if prime_arr[val]:
            num += 1
        
print(num)