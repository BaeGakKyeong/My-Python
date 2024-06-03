#매개변수에 디폴트 값을 두개 사용한 div() 함수

def div(n = 1, m = 2) :
    return n / m

print('div() =', div())
print('div(4) =', div(4))
print('div(6, 3) =', div(6, 3))