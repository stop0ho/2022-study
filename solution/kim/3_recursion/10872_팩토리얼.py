def fac(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return n*fac(n-1)
num=int(input())
print(fac(num))
