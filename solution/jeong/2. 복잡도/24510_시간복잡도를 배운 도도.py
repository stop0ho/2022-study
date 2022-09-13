# 'for'과 'while'의 개수를 세면 되는 문제
'''
Q1. 파이썬은 문자열에서 특정 문자열의 개수를 아는 함수가 있나?
A1. 가능하다. str.count('문자열') 사용
'''

c = int(input())

m = 0
for i in range(c):
    count = 0
    user_input = input()
    count += user_input.count('for')
    count += user_input.count('while')
    if count > m:
        m = count

print(m)
