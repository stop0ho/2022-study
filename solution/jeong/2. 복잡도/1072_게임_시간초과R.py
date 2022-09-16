x, y = map(int, input().split())
cnt = 0
z = int(y/x * 100)
while True:
    if x <= y:
        print(-1)
        break
    
    if z != int(y/x * 100):
        print(cnt)
        break
    
    x += 1
    y += 1
    cnt += 1