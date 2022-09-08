flag = True
while(flag):
    A, B = map(int, input().split())
    if(A == 0 and B == 0):
        flag = False
    else:
        print(A+B)