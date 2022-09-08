N, S = map(int, input().split())
input_list = list(map(int, input().split()))

def DFS(index, start):
    global N, S, input_list
    val = 0
    
    if index == N:
        return 0
    if start + input_list[index] == S:
        val += 1
    
    val += DFS(index+1, start)
    val += DFS(index+1, start+input_list[index])
    
    return val

print(DFS(0,0))