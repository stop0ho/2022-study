def Fibo(num):
    if num==1: return 0
    elif num==2: return 1
    else:
        return Fibo(num-1)+Fibo(num-2)

print(Fibo(int(input())))
