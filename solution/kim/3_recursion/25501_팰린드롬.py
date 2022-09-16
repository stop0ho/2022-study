T=int(input()) #문자 개수
for _ in range(T):
    s=input()
    cnt=0
    flag=1 

    for i in range(round(len(s)/2)):
        if s[i]==s[-i-1]:
            cnt+=1
        else:
            cnt+=1
            flag=0 #팰린드롬 아님
            break

    print(flag,cnt)