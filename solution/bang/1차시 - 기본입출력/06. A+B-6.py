T = int(input())
for i in range(0, T):
    # input().split(',') : 입력받은 값을 콤마를 기준으로 분리
    A, B = map(int, input().split(','))
    print(A+B)