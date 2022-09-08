# 골드바흐의 추측 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.

# test case와 입력 값을 받아들인다.
T = int(input())

l = []
for i in range(T):
    l.append(int(input()))
    
# max를 활용해서 list 안에서 가장 큰 값을 찾아낸다.
max = l[0]
for i in l:
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

for val in l:
    a, b = val//2, val//2
    while a > 1:
        if prime_arr[a] and prime_arr[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1