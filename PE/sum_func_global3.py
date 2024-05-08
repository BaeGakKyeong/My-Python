#함수 내부에서 값을 변경하고, 그 값을 외부에서 확인하기

def print_sum() :
    a = 100
    b = 200     #함수 내부에서 값을 할당하면 지역변수(local variable)가 생성된다. 
    result = a + b
    print('print_sum() 내부 : {} 와 {} 의 합은 {} 입니다.'.format(a, b, result))
    
a = 10
b = 20
print_sum()
result = a + b
print('print_sum 외부 : {} 와 {} 의 합은 {} 입니다.'.format(a, b, result))

#이처럼, 구현한 함수 안에 있는 변수는 외부에서 선언된 변수와 독립적이다. 