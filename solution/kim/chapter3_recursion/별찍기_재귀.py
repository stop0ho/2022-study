def draw(n, idx):
    if n == 1: #n이 1이면 하나만 출력
        starMap[idx][idx] = '*'
        return
    l = 4 * n -3 #가장 밖 테두리 길이 (4n-3 x 4n-3모양 정사각형)
    for i in range(idx, l+idx): #x,y좌표를 2씩 더해줌(작은 사각형)
        starMap[idx][i] = '*'
        starMap[idx+l-1][i] = '*'
        starMap[i][idx] = '*'
        starMap[i][idx+l-1] = '*' 
 
    return draw(n-1, idx+2) #재귀로 변경할 조건
    
    
n = int(input())
lens = 4 * n -3

starMap = [[' '] * lens for _ in range(lens)]
#2차원 배열을 바로 만드는 법
draw(n,0) #idx를 재귀로 변경해야할 것

#출력
for i in range(lens):
    for j in range(lens):
        print(starMap[i][j], end="")
    print()