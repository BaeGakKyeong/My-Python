#매개변수를 사용하지 않고 외부 변수를 사용하는 경우

def print_sum() :   #매개변수 지정 안함
    result = a + b
    print('print_sum() 내부 : {} 와 {} 의 합은 {} 입니다.' .format(a, b, result))
    
a = 10
b = 20      #함수 외부에서 매개변수 선언, 전역변수(glabal variable)
print_sum() #인자를 선언 안함
result = a + b
print('print_sum 외부 : {} 과 {} 의 합은 {} 입니다.'.format(a, b, result))