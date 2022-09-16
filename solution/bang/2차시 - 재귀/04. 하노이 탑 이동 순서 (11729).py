def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, temp, end)
    print(start, end)
    hanoi(n-1, temp, end, start)
    
K = int(input())
print(2**K-1)
hanoi(K, 1, 3, 2)