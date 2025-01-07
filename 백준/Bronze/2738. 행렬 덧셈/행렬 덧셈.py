N, M = map(int, input().split())

A = []
B = []
    
for i in range(N):
    A.append(list(map(int, input().split())))
    
for i in range(N):
    B.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(M):
        print(str(A[i][j] + B[i][j])+" ", end="")
            
            #ㅏ어라ㅓㅇ나럼알마닝차ㅣㅇ므창츠아니츠ㅏㅣㅇㄴ츠ㅏ인 나한테 왜 이런 시련을.....


