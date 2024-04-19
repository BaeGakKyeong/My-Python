#이중 조건문

num = int(input('정수를 입력하시오 : '))

#외 if-else문
if num < 0 :
    print(num, '은(는) 음수입니다.')
    
else :
    print(num, '은(는) 음수가 아닙니다.')
    
    #내부 if-else문
    if num % 2 == 1 :
        print(num, '은(는) 홀수입니다.')
        
    else :
        print(num, '은(는) 짝수입니다.')