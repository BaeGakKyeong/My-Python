#윤년을 판단하는 프로그램

year = int(input('년도를 입력하시오 :'))

if year % 4 == 0 :
    
    if year % 100 == 0 :
        
        if year % 400 == 0 :
            print('윤년입니다.')
            
        else :
            print('윤년이 아닙니다.')
        
    else :
        print('윤년입니다.')
    
else :
    print('윤년이 아닙니다.')
    