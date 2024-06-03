#가변 인자(arbitrary argument)를 가지는 함수의 정의와 호출

def greet(*names) :
    for name in names :
        print('안녕하세요', name, '씨')
        
greet('홍길동', '양만춘', '이순신')     #인자가 세개
greet('James', 'Thomas')           #인자가 네개