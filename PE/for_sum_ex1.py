#연속적인 값의 생성과 누적 덧셈

x = int(input('자연수를 입력하시오 : '))
s = 0   #변수 초기화를 반드시 해 주어야 한다

for i in range(1, x + 1) :  #range 함수에 변수와 수식을 넣어도 작동한다.
    print(s, '+', i, '=', end = ' ')
    s += i
    print(s)
    
print('1부터', x, '까지의 합은', s, '입니다.')