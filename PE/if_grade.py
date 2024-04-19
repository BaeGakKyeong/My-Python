#점수에 때라 성적을 산출하는 프로그램

score = int(input('100 이하의 자연수를 입력하시오 :'))

if score >= 90 :
    grade = 'A'

else :
    if score >= 80 :
        grade = 'B'
    else:
        if score >= 70 :
            grade = 'C'
            
        else:
            if score >= 60 :
                grade = 'D'
                
            else :
                grade = 'F'
    
print(score, '점은', grade, '입니다.')