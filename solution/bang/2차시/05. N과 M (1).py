# 입력값 N과 M을 받아들인다.
N, M = map(int, input().split())

# 백트래킹(DFS) 사용
l = []

def permutation():
    # l에 M개의 중복되지 않는 값이 모두 찾을 경우
    # 출력하는 코드
    if len(l) == M:
        print(' '.join(map(str, l)))
        return
    
    # DFS를 통해 모든 순열을 만들어 내는 코드
    for i in range(1, N+1):
        if i in l:
            continue # list에 이미 값이 있는 경우 바로 다음로 넘어감 (아래 코드 작도 안됨.)
        l.append(i)
        permutation()
        l.pop()

permutation()