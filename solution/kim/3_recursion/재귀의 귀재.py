st=input()
cnt=0

def recursion(s, l, r):
    global cnt #전역변수를 함수에서 사용하는 법
    cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

print(isPalindrome(st),cnt) #,가 자동으로 띄어쓰기 하나 됨