#세 정수를 입력받아 그 중에서 당첨번호 2, 3, 9가 몇개 있는지에 따라 상금을 출력하는 프로그램

a = int(input('세 정수를 입력하시오'))
b = int(input('세 정수를 입력하시오'))
c = int(input('세 정수를 입력하시오'))

#a, b, c를 큰 순서대로 각각 lar_num, mid_num, sho_num에 대입, 만약 같은 수가 있울 경우 한개의 값은 버림.
if a > b :
    if a > c :
        lar_num = a
        if b > c :
            mid_num = b
            sho_num = c
        elif b < c :
            mid_num = c
            sho_num = b
    elif a < c :
        lar_num = c
        mid_num = a
        sho_num = b
    else :
        lar_num = a
        sho_num = b
        mid_num = 0
elif a < b :
    if a < c :
        sho_num = a
        if b > c :
            lar_num = b
            mid_num = c
        elif b < c :
            lar_num = c
            mid_num = b
    elif a > c :
        sho_num = c
        mid_num = a
        lar_num = b
    else : 
        lar_num = b
        sho_num = a
        mid_num = 0
else :
    if a > c : 
        sho_num = c
        lar_num = a
        mid_num = 0
    elif a < c :
        lar_num = c
        sho_num = a
        mid_num = 0
    else :
        lar_num = a
        sho_num = 0
        mid_num = 0
    
#맞은 개수에 따라 상금을 출력
if lar_num == 9 : 
    if mid_num == 3 :
        if sho_num == 2 : 
            print('상금 1억원')
        else :
            print('상금 1천만원')
    elif sho_num == 2 : 
        print('상금 1천만원')
    else :
        print('상금 1만원')
else :
    if mid_num == 3 :
        if sho_num == 2 :
            print('상금 1천만원')
        else :
            print('상금 1만원')
    else :
        if sho_num == 2 :
            print('상금 1만원')
        else :
            print('다음 기회에...')
            
#논리 오류 발생... GG
