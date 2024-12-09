str = input() #문자열 입력
result ="" #결과 저장 빈 문자열

for char in str: #입력 문자열의 각 문자를 변환
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()
        
print(result)
    


