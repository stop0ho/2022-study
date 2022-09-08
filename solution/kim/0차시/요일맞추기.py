#1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지
cld=[31,28,31,30,31,30,31,31,30,31,30,31]
d=['MON','TUE','WED','THU','FRI','SAT','SUN'] 
sum=0
x,y=map(int,input().split())
for i in range(x-1): #1월이면 안더해져야 함
    sum+=cld[i] 
sum+=y-1 #2일부터 1일 차이남

ans=d[sum%7] #7로 나눈 나머지가 0일때 월요일이 될 수 있게 리스트 순서 변경
print(ans)