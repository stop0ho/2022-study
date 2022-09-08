list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
val = 0
x, y = map(int, input().split())
for i in range(1, x):
    if(i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12):
        val += 31
    elif(i == 4 or i == 6 or i == 9 or i == 11):
        val += 30
    elif(i == 2):
        val += 28
val += y
print(list[val%7])