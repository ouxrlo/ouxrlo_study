def solution(n):
    # 이차원 배열 생성 [0]*n n개의 0으로 이루어짐
    array = [[0] * n for _ in range(n)]
    
    # 방향 정의 (오른쪽, 아래, 왼쪽, 위쪽) , x 마이너스 축에 머리 두고 엎드려있다고 생각
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move_direction = 0  # 현재 방향 (처음에는 오른쪽)
    
    # 초기 위치와 숫자 설정
    x, y = 0, 0  # 시작 위치
    num = 1      # 시작 숫자
    
    
     
    while num <= n*n: #행렬 수보다 작거나 같아야함
        array[x][y] = num # 지금 위치에 숫자 너어줌
        num += 1 # 위치는 1씩 증가
        
        
        # 이동할 위치 (dx,dy)
        now_x, now_y = directions[move_direction]
        
        # 현재 위치에서 이동할 위치의 값 합 (nx, ny)
        later_x, later_y = x+now_x, y+now_y
        
        
        # 그 위치에 못갈수도 있으니 이동 가능한지
        if 0<=later_x<n and 0<=later_y<n and array[later_x][later_y] == 0:
            x,y = later_x, later_y
            
        else:
            # 이동이 안되는것도 있ㅔ겟지 몰라 막해
            move_direction = (move_direction+1)%4
            now_x, now_y = directions[move_direction]
            x,y = x+now_x, y+now_y
            
    return array
        
    
