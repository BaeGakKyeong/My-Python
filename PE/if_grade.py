#점수에 때라 성적을 산출하는 프로그램

score = int(input('100 이하의 자연수를 입력하시오 :'))

if score >= 90 :
    grade = 'A'
if score < 90 and score >= 80 :
    grade = 'B'
if score < 80 and score >= 70 :
    grade = 'C'
if score < 70 and score >= 60 :
    grade = 'D'
if score < 60 : 
    grade = 'F'
    
print(score, '점은', grade, '입니다.')