def solution(n):
    # 이차원 배열 생성 [0]*n n개의 0으로 이루어짐
    array = [[0] * n for _ in range(n)]
    
    # 방향 정의 (오른쪽(3시), 아래(6시), 왼쪽(9시), 위쪽(12시)) 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 현재 방향 (처음에는 오른쪽(3시))
    move_direction = 0  
    
    # 초기 위치와 숫자 설정
    x, y = 0, 0  # 시작 위치
    num = 1      # 시작 숫자
    
    
     
    while num <= n*n: #행렬 수보다 작거나 같아야함, 크면 행렬 벗어남
        array[x][y] = num # 지금 위치에 숫자 너어줌
        num += 1 # 위치는 1씩 증가
        
        
        # 이동할 방향값 now_로 치환
        now_x, now_y = directions[move_direction]
        
        # 현재 위치에서 이동 할 방향값 later_로 치환
        later_x, later_y = x+now_x, y+now_y
        
        
        # 내가 이동 할 예정인 위치가 갈 수 있는 범위안에 있는지, 방문하지 않은곳인지
        if 0<=later_x<n and 0<=later_y<n and array[later_x][later_y] == 0:
            # 만약 유효한 위치라면 아래의 식으로 업데이트
            x,y = later_x, later_y
            
        else:
            # 아 갔는데 못가는 길이래 다른길 찾으셈
            move_direction = (move_direction+1)%4 #현재 위치에서 +1이동했는데 못가는 경우의수 (방법은 4가지라 나눔)
            now_x, now_y = directions[move_direction]
            x,y = x+now_x, y+now_y 
            
    return array
        
    
