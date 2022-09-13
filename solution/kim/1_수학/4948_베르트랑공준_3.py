inputList = list()

N = 123456*2 + 1 #입력값 조건이 있으니까 거기에 맞게 소수 리스트 생성
isPrime = [True] * N #True가 N개 있는 리스트 생성

for i in range(2, int(N**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, N, i):
            isPrime[j] = False    #True만 있는 리스트에 소수가 아닌애들은 false


def counting(inputValue):
    cnt = 0
    for k in range(inputValue+1, inputValue*2 + 1):
        if isPrime[k]:
            cnt += 1
    print(cnt)


while True:
    k = int(input())

    if not k: #0이면 break로 반복문 나옴 (==0으로 해도 ㄱㅊ)
        break
    counting(k)