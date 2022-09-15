from itertools import combinations as cb

#0이 나올때까지 돌아감.
while True:
    s=list(map(int,input().split()))
    k=s[0] #처음 수는 리스트 길이
    lst=s[1:] #남은 값은 뽑을 값 리스트

    if k==0:
        break

    for i in cb(lst,6): #로또는 6개의 수를 뽑으므로
        for j in i:
            print(j,end=' ') #튜플로 출력되는 애를 띄어쓰기로 바꾸기
        print()
    print()