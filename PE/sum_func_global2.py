#함수 외부에서 정의된 값을 함수 내부에서 변경하는 경우

def print_sum() :
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부 : {} 와 {} 의 합은 {} 입니다.'.format(a, b, result))
    
a = 10
b = 20      #함수 외부에서 변수 변경
print_sum()

#함수 내부에서 선언된 변수는 외부에서 변경할 수 없다