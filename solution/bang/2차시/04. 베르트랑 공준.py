# 리스트 생성
input_list = []

# 입력값 받기
while(True):
    a = int(input())
    if(a == 0):
        break
    else:
        input_list.append(a)

if input_list is not None:
    # 처음에는 바로 반복문을 사용해서 구현했더니 
    # 계산 시간이 너무 길어서 오류 발생
    # 따라서 input_list 내에서 가장 큰 값으로 
    # prime_arr를 만들기로 결정함.
    max = input_list[0]
    for i in input_list[0:]:
        if max < i:
            max = i
 
    # 에라토스테네스의 체 활용

    # 소수인지 판별하기 위한 배열 생성(주어지는 수는 1000이하의 자연수임.)
    prime_arr = [True]*(2*max+1)
    prime_arr[0] = False
    prime_arr[1] = False

    # 반복문을 통해서 소수를 모두 찾아냄
    for i in range(2, 2*max+1):
        if prime_arr[i] == True: #특정 값이 아직까지 소수인 경우
            j = 2
            while(i*j) <= 2*max:
                prime_arr[i*j] = False # i의 배수 값을 소수가 아니라고 판별
                j += 1 

    # n부터 2n까지의 소수를 출력
    for n in input_list[0:]:
        num = 0 # 소수의 개수 초기값
        for i in range(n+1, 2*n+1):
            if prime_arr[i]:
                num += 1 
        print(num)