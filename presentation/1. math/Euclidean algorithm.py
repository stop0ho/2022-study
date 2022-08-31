def uclid(a, b):
    r = a % b
    if r == 0:      #종료조건
        return b
    else:
        return uclid(b, r)
        
print(uclid(106, 16))
print(uclid(1071, 1029))