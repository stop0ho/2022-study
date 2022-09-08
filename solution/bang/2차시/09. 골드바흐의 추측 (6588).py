# 리스트 생성
input_list = []

# 입력값 받기
while(True):
    a = int(input())
    if(a == 0):
        break
    else:
        input_list.append(a)

# max를 활용해서 list 안에서 가장 큰 값을 찾아낸다.
max = input_list[0]
for i in input_list:
    if max < i:
        max = i

# 에라토스테네스의 체를 활용해서 소수 list를 만든다.
prime_arr = [True]*(max+1)
prime_arr[0] = False
prime_arr[1] = False

for i in range(2, max+1):
    if prime_arr[i] == True:
        j = 2
        while(i*j) <= max:
            prime_arr[i*j] = False
            j += 1

for val in input_list:
    a, b = 3, val-3
    while a <= b:
        if prime_arr[a] and prime_arr[b]:
            print(val, '=', a, '+', b)
            break
        else:
            a += 2
            b -= 2
    if a > b:
        print("Goldbach's conjecture is wrong.")