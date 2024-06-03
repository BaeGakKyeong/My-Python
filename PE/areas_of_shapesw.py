#직사각형과 원의 면적을 구하는 함수의 구현, 위치 인자와 키워드 인자의 혼용

def func(shape, width = 1, height = 1, radius = 1) :
    if shape == 0 :     #shape가 0이면 사각형의 면적을 반환
        return width * height
    if shape == 1 :     #shape가 1이면 원의 면적을 반환
        return radius ** 2 * 3.14
    
print('rect area =', func(0, width = 10, height = 2))
print('circle area =', func(1, radius = 5))