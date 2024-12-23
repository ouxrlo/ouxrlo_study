# num_list에서 마지막 원소(리스트의 맨 뒤에 있는 원소)가 그 전 원소(마지막 원소 바로 앞의 원소)보다 클 때, 두 값을 뺀 차이 리스트 추가
# 그 전 원소가 마지막 원소보다 크거나 같으면, 마지막 원소의 두 배를 리스트 추가
def solution(num_list):
    answer = []
    if num_list [-1]> num_list[-2]:
        num_list.append(num_list[-1] - num_list [-2])
    else:
        num_list [-2]>= num_list[-1]
        num_list.append(num_list[-1] *2)
    return num_list