#함수 내부에서 값을 변경하고, 그 값을 외부에서 확인하기

def print_sum() :
    global a, b #global 키워드는 함수 내부의 변수(local variable)라도 전역변수(global variable)로 만든다.
    a = 100
    b = 200     #함수 내부에서 값을 할당하면 지역변수(local variable)가 생성된다. 위에서 global 키워드를 사용했으므로 전역변수가 된다. 
    result = a + b
    print('print_sum() 내부 : {} 와 {} 의 합은 {} 입니다.'.format(a, b, result))
    
a = 10
b = 20
print_sum()
result = a + b
print('print_sum 외부 : {} 와 {} 의 합은 {} 입니다.'.format(a, b, result))

"""
이처럼, 구현한 함수 안에 있는 변수는 외부에서 선언된 변수와 독립적이다. 
단, global a = 100과 같이 할당문에서는 사용할 수 없고, 변수를 할당하기 전에 사용해야 한다. 
긴 코드에서 전역변수의 사용은 오류를 일으킬 가능성이 높으므로, 가급적 피하는 것이 좋다. 
"""